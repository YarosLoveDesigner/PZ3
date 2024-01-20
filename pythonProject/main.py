#class Cabinet():
#    def __init__(self, Name, S):
#        self.Name = Name
#       self.S = S
#
#   def __str__(self):
#        return f"Name: {self.Name}, S: {self.S}"

# Ввод значений с клавиатуры
#name_input = input("Введите имя ответственного за кабинет: ")
#s_input = input("Введите площадь кабинета: ")

# Создание объекта класса с введенными значениями
#Cob1 = Cabinet(Name=name_input, S=s_input)

# Вывод информации о объекте
#print(Cob1)


class Cabinet():
    def __init__(self, manager_name, area):
        self.manager_name = manager_name
        self.set_area(area)

    def set_area(self, area):
        if 10 <= area <= 100:
            self.area = area
        else:
            raise ValueError("Площадь кабинета должна быть от 10 кв м до 100 кв м")

    def __str__(self):
        return f"Зав. кабинетом: {self.manager_name}, Площадь: {self.area} кв.м"


# Ввод значений с клавиатуры
manager_name_input = input("Введите имя зав. кабинетом (в формате Фамилия И.О.): ")
area_input = int(input("Введите площадь кабинета (от 10 до 100 кв м): "))

# Создание объекта класса с введенными значениями
try:
    Cob1 = Cabinet(manager_name=manager_name_input, area=area_input)
    # Вывод информации о объекте
    print(Cob1)
except ValueError as e:
    print(f"Ошибка: {e}")

