def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        number1 = 10
        number2 = 5
        result = is_strictly_greater(number1, number2)
        print(result)
        number1 = 3
        number2 = 7
        result = is_strictly_greater(number1, number2)
        print(result)
        number1 = 8
        number2 = 8
        result = is_strictly_greater(number1, number2)
        print(result)
    except Exception as e:
        print(f'An error occurred: {e}')