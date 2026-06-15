def sort_pair(a, b):
    return tuple(sorted((a, b)))
if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = sort_pair(num1, num2)
    print(result)
    num3 = -3
    num4 = 7
    result2 = sort_pair(num3, num4)
    print(result2)
    num5 = 42
    num6 = 42
    result3 = sort_pair(num5, num6)
    print(result3)