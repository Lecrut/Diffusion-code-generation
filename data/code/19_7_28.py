def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        value1 = 10
        value2 = 5
        result = is_strictly_greater(value1, value2)
        print(result)
    except Exception as e:
        print(e)