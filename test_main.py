
def test_greeting():
    """
    Программа которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Формируем нужную строку
    output = "Привет, {0}! Тебе {1} лет.".format(name, str(age))

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Программа которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO считаем периметр
    perimeter = (a + b) * 2

    assert perimeter == 60

    # TODO считаем площадь
    area = a * b

    assert area == 200


def test_circle():
    """
    Программа которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    from math import pi
    r = 23
    # TODO считаем площадь
    area = pi * r ** 2

    assert area == 1661.9025137490005

    # TODO считаем длину окружности
    length = (pi * 2) * r

    assert length == 144.51326206513048


def test_random_list():
    """
    Cписок из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создаем список
    import random
    l = []

    for _ in range(0, 10):
        l_1 = random.randrange(0, 101)
        l.append(l_1)

    # Добавил сортировку списка через переменную
    mu_list = sorted(l)

    assert len(l) == 10
    assert all(mu_list[i] <= mu_list[i + 1] for i in range(len(mu_list) - 1))


def test_unique_elements():
    """
    Удалили из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалили повторяющиеся элементы
    l = list((set(l)))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Cловарь из двух списков.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создали словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second