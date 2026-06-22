def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        value1 = 10
        value2 = 5
        result = is_strictly_greater(value1, value2)
        print(result)
        value1 = 3
        value2 = 7
        result = is_strictly_greater(value1, value2)
        print(result)
    except ValueError as e:
        print(e)