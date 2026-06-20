def high_precision_subtraction(x, y):
    return x - y

if __name__ == '__main__':
    value1 = 23.4567890123456789
    value2 = 12.3456789012345678
    result = high_precision_subtraction(value1, value2)
    print(result)