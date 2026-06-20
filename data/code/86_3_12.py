def compare_booleans(a, b):
    return [a == b]

if __name__ == '__main__':
    sample1 = (True, False)
    result1 = compare_booleans(*sample1)
    print(result1)

    sample2 = (True, True)
    result2 = compare_booleans(*sample2)
    print(result2)

    sample3 = (False, True)
    result3 = compare_booleans(*sample3)
    print(result3)