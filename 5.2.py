def maxnumber(num1, num2):
    """Определяет какое из двух введенных int чисел больше"""
    if num1 > num2:
        return num1
    else:
        return num2

number1, number2 = map(int, input('Введите два целых числа: ').split( ))
print('Большее число: ', maxnumber(number1, number2))
