def abs_diff(a, b):
    return ((a - b) ^ (a - b >> 31)) & 4294967295

if __name__ == '__main__':
    num1 = 15
    num2 = 8
    result = abs_diff(num1, num2)
    print(result)