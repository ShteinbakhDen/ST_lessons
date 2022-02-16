from random import randrange

x1 = randrange(10) + 1
print(x1)

a = -1
b = 0
while a != x1:
    a = int(input('Введите целое число от 1 до 10 '))
    b += 1
    if a < 0:
        print('Введите положительное число')
    elif a > x1:
        print('Загаданное число меньше')
    elif a < x1:
        print('Загаданное число больше')
print('Вы отгадали число с', b, 'попытки, поздравляю')
