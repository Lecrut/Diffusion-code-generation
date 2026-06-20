def abs_diff(a, b):
    return (a - b) & ((a - b) >> 31)

if __name__ == '__main__':
    num1 = 2**64 - 10
    num2 = 5
    result = abs_diff(num1, num2)
    print(result)