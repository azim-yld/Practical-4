a = int(input("Введите номер первого цвета: 1-красный, 2-желтый, 3-синий "))
b = int(input("Введите номер второго цвета: 1-красный, 2-желтый, 3-синий "))

if a == 1 and b == 1:
    print("Красный")
elif a == 2 and b == 2:
    print("Желтый")
elif a == 3 and b == 3:
    print("Синий")
elif a == 1 and b == 2:
    print("Оранжевый")
elif a == 2 and b == 1:
    print("Оранжевый")
elif a == 1 and b == 3:
    print("Фиолетовый")
elif a == 3 and b == 1:
    print("Фиолетовый")
elif a == 2 and b == 3:
    print("Зеленый")
elif a == 3 and b == 2:
    print("Фиолетовый")
else:
    print("Ошибка")