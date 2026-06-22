def compare_values(a, b):
    difference = a - b
    if difference < 0:
        return -1
    elif difference > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    result1 = compare_values(7, 3)
    print(result1)
    result2 = compare_values(4, 4)
    print(result2)
    result3 = compare_values(9, 15)
    print(result3)