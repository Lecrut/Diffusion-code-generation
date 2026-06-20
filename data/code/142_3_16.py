def compare_booleans(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    result2 = compare_booleans(False, False)
    result3 = compare_booleans(True, False)
    print(result1)
    print(result2)
    print(result3)