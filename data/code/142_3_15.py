def compare_booleans(a, b):
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    result2 = compare_booleans(False, False)
    result3 = compare_booleans(True, False)
    print(result1 and result2 or result3)