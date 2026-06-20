def abs_diff(a, b):
    return (a - b) & ((a - b) >> 31)

if __name__ == '__main__':
    num1 = 1234567890123456789
    num2 = 9876543210987654321
    result = abs_diff(num1, num2)
    print(result)