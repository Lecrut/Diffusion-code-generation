def are_both_true(val1, val2):
    if not isinstance(val1, bool) or not isinstance(val2, bool):
        raise ValueError("Both inputs must be boolean values")
    return val1 and val2

if __name__ == '__main__':
    print(are_both_true(True, True))
    print(are_both_true(False, True))
    print(are_both_true(True, False))
    print(are_both_true(False, False))