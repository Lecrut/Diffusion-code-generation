def compare_booleans(a, b):
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(True, False)
    result2 = compare_booleans(False, True)
    print(result1 and result2)