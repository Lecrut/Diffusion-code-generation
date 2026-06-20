def compare_booleans(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    result2 = compare_booleans(False, False)
    print(result1 and result2)