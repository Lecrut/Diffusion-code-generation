def compare_booleans(x, y):
    return [x == y]

if __name__ == '__main__':
    sample1 = (True, False)
    result1 = compare_booleans(*sample1)
    print(result1)

    sample2 = (False, False)
    result2 = compare_booleans(*sample2)
    print(result2)

    sample3 = (True, True)
    result3 = compare_booleans(*sample3)
    print(result3)