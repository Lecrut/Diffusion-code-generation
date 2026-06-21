def compare_values(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result1 = compare_values(10, 2)
    print(result1)
    result2 = compare_values(6, 6)
    print(result2)
    result3 = compare_values(1, 9)
    print(result3)