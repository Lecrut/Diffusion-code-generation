def find_min_max(a, b):
    if a <= b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    result = find_min_max(num1, num2)
    print(result)
    num3 = 42
    num4 = 99
    result2 = find_min_max(num3, num4)
    print(result2)
    num5 = 10
    num6 = 10
    result3 = find_min_max(num5, num6)
    print(result3)