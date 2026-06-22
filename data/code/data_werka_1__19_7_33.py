def is_strictly_greater(num1, num2):
    return num1 > num2
if __name__ == '__main__':
    try:
        value1 = 10
        value2 = 5
        result = is_strictly_greater(value1, value2)
        print(result)
        value3 = 'a'
        value4 = 3
        result = is_strictly_greater(value3, value4)
    except TypeError as e:
        print(e)