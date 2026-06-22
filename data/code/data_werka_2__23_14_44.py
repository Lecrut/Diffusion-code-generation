def compare_values(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1
if __name__ == '__main__':
    result = compare_values(5, 3)
    print(result)
    result = compare_values(2, 2)
    print(result)
    result = compare_values(7, 10)
    print(result)