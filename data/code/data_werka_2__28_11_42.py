def is_larger(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    value1 = 15
    value2 = 7
    result1 = is_larger(value1, value2)
    print(result1)

    value3 = -3
    value4 = -8
    result2 = is_larger(value3, value4)
    print(result2)

    value5 = 0
    value6 = 0
    result3 = is_larger(value5, value6)
    print(result3)