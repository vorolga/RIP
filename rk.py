# Вариант В.
#
#     1. «Операционная система» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список всех компьютеров, у которых название начинается с буквы «А», и их операционные системы.
#
#     2. «Операционная система» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список ОС с минимальной памятью компьютеров для каждой ОС, отсортированный по минимальной памяти.
#
#     3. «Операционная система» и «Компьютер» связаны соотношением многие-ко-многим.
#     Выведите список всех связанных компьютеров и ОС,  отсортированный по компьютерам, сортировка по ОС производная.

from operator import itemgetter


class OS:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Computer:
    def __init__(self, id, brand, memory_gb, os_id):
        self.id = id
        self.brand = brand
        self.memory_gb = memory_gb
        self.os_id = os_id


class ComputerOS:
    def __init__(self, computer_id, id_os):
        self.computer_id = computer_id
        self.id_os = id_os


operating_system = [
    OS(1, 'Windows 10'),
    OS(2, 'Linux Ubuntu 21.10'),
    OS(3, 'MacOS Big Sur 11.6'),
    OS(11, 'Windows 8'),
    OS(22, 'Linux Ubuntu 20.04'),
    OS(33, 'MacOS Big Sur 11.5'),
]

computers = [
    Computer(1, 'Asus', 64, 2),
    Computer(2, 'Lenovo', 128, 2),
    Computer(3, 'Acer', 128, 1),
    Computer(4, 'Dell', 64, 1),
    Computer(5, 'Acer', 256, 2),
    Computer(6, 'HP', 128, 1),
    Computer(7, 'Apple', 128, 3),
    Computer(8, 'Xiaomi', 256, 1),
    Computer(9, 'Apple', 512, 3),
]

computers_os = [
    ComputerOS(1, 2),
    ComputerOS(2, 2),
    ComputerOS(3, 1),
    ComputerOS(4, 1),
    ComputerOS(5, 2),
    ComputerOS(6, 1),
    ComputerOS(7, 3),
    ComputerOS(8, 1),
    ComputerOS(9, 3),
    ComputerOS(1, 22),
    ComputerOS(2, 22),
    ComputerOS(3, 11),
    ComputerOS(4, 11),
    ComputerOS(5, 22),
    ComputerOS(6, 11),
    ComputerOS(7, 33),
    ComputerOS(8, 11),
    ComputerOS(9, 33),
]


def main():
    one_to_many = [(comp.brand, comp.memory_gb, os.name)
                   for comp in computers
                   for os in operating_system
                   if comp.os_id == os.id]

    many_to_many_temp = [(os.name, comp_os.computer_id, comp_os.id_os)
                         for os in operating_system
                         for comp_os in computers_os
                         if os.id == comp_os.id_os]

    many_to_many = [(comp.brand, os_name)
                    for os_name, comp_id, os_id in many_to_many_temp
                    for comp in computers if comp.id == comp_id]

    print('\n\nЗадание В1')
    res = list(filter(lambda i: str(i[0]).startswith('A'), one_to_many))
    res = [
        (elem[0], elem[2])
        for elem in res
    ]
    print(res)

    print('\n\nЗадание В2')
    res = sorted(one_to_many, key=itemgetter(1))
    res = [
        (elem[2], elem[1])
        for elem in res
    ]
    print(res)

    print('\n\nЗадание В3')
    res = sorted(many_to_many, key=itemgetter(0))
    print(res)
    print('\n\n')


if __name__ == '__main__':
    main()
