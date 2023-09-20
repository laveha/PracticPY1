import math

def get_number_input(p):
    while True:
        try:
            a = float(input(p))
            return a
        except ValueError:
            print("Ошибка: Введите числовое значение.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")

    b = input("Введите номер операции: ")

    if b == '0':
        break
    elif b in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        if b == '1':
            c = get_number_input("Введите первое число: ")
            d = get_number_input("Введите второе число: ")
            e = c + d
        elif b == '2':
            c = get_number_input("Введите первое число: ")
            d = get_number_input("Введите второе число: ")
            e = c - d
        elif b == '3':
            c = get_number_input("Введите первое число: ")
            d = get_number_input("Введите второе число: ")
            e = c * d
        elif b == '4':
            c = get_number_input("Введите делимое: ")
            d = get_number_input("Введите делитель (не ноль): ")
            if d != 0:
                e = c / d
            else:
                print("Ошибка: Деление на ноль.")
                continue
        elif b == '5':
            c = get_number_input("Введите число: ")
            f = get_number_input("Введите степень: ")
            e = c ** f
        elif b == '6':
            a = get_number_input("Введите число: ")
            if a >= 0:
                e = math.sqrt(a)
            else:
                print("Ошибка: Квадратный корень из отрицательного числа.")
                continue
        elif b == '7':
            a = get_number_input("Введите целое неотрицательное число: ")
            if a.is_integer() and a >= 0:
                e = factorial(int(a))
            else:
                print("Ошибка: Факториал определен только для целых неотрицательных чисел.")
                continue
        elif b == '8':
            g = get_number_input("Введите угол в градусах: ")
            e = math.sin(math.radians(g))
        elif b == '9':
            g = get_number_input("Введите угол в градусах: ")
            e = math.cos(math.radians(g))
        elif b == '10':
            g = get_number_input("Введите угол в градусах: ")
            e = math.tan(math.radians(g))

        print(f"Результат: {e}")
    else:
        print("Ошибка: Введите корректный номер операции.")