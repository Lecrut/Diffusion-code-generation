def is_greater(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    value1 = 0.1 + 0.2
    value2 = 0.3
    if is_greater(value1, value2):
        print("value1 is greater")
    else:
        print("value2 is greater or equal")

    value3 = 0.45
    value4 = 0.44999999999999996
    if is_greater(value3, value4):
        print("value3 is greater")
    else:
        print("value4 is greater or equal")