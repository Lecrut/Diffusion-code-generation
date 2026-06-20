def subtract_precise(a, b):
    return a - b

if __name__ == '__main__':
    value1 = 1234567890.123456789
    value2 = 987654321.987654321
    result = subtract_precise(value1, value2)
    print(result)