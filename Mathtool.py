"""
Запуск:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие MAX_COEFFICIENT.
"""

import math
import sys

MAX_COEFFICIENT = 10000



def show_help():
    """Вывод справки."""
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print()
    print(f"Коэффициенты A, B, C — целые числа, по модулю не превышающие {MAX_COEFFICIENT}.")


def read_arguments(params):
    if len(params) == 0 or params[0] == "--help":
        show_help()
        sys.exit(0)

    if params[0] != "solve":
        print("ОШИБКА: неизвестная команда", file=sys.stderr)
        sys.exit(1)

    if len(params) == 1:
        a_text = input("Введите A: ")
        b_text = input("Введите B: ")
        c_text = input("Введите C: ")
    elif len(params) == 7:
        if params[1] != "-a" or params[3] != "-b" or params[5] != "-c":
            print("ОШИБКА: неизвестный параметр", file=sys.stderr)
            sys.exit(1)
        a_text = params[2]
        b_text = params[4]
        c_text = params[6]
    else:
        print("ОШИБКА: неверный набор параметров", file=sys.stderr)
        sys.exit(1)

    return a_text, b_text, c_text


def to_integers(a_text, b_text, c_text):
    try:
        a = int(a_text)
        b = int(b_text)
        c = int(c_text)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)
    return a, b, c


def check_range(a, b, c):
    if abs(a) > MAX_COEFFICIENT or abs(b) > MAX_COEFFICIENT or abs(c) > MAX_COEFFICIENT:
        print(f"ОШИБКА: значение вне допустимого диапазона. "
              f"Допустимый диапазон от {-MAX_COEFFICIENT} до {MAX_COEFFICIENT}",
              file=sys.stderr)
        sys.exit(1)


def solve_linear(b, c):
    if b != 0:
        print("Уравнение линейное")
        root = -c / b
        print(f"x = {root:.3f}")
    else:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)


def solve_quadratic(a, b, c):
    print("Уравнение квадратное")

    discriminant = b * b - 4 * a * c
    print(f"D = {discriminant}")

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {root1:.3f}")
        print(f"x2 = {root2:.3f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"x = {root:.3f}")
    else:
        print("Действительных корней нет")


def solve_equation(a, b, c):
    if a == 0:
        solve_linear(b, c)
    else:
        solve_quadratic(a, b, c)


def main():
    a_text, b_text, c_text = read_arguments(sys.argv[1:])
    a, b, c = to_integers(a_text, b_text, c_text)
    check_range(a, b, c)
    solve_equation(a, b, c)
    sys.exit(0)


if __name__ == "__main__":
    main()
