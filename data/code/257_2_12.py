def abs_diff(a, b):
    return ((a - b) ^ ((a - b) >> 31)) & 0xFFFFFFFF

if __name__ == '__main__':
    num1 = 7
    num2 = -4
    result = abs_diff(num1, num2)
    print(result)