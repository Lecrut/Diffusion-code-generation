def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        number1 = 10
        number2 = 5
        result = is_strictly_greater(number1, number2)
        print(result)
    except ValueError as e:
        print(e)