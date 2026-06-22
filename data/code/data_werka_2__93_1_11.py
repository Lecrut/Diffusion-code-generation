def are_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return a is False and b is False

if __name__ == '__main__':
    val1 = are_both_false(False, False)
    val2 = are_both_false(True, False)
    val3 = are_both_false(False, True)
    val4 = are_both_false(True, True)
    print(val1)
    print(val2)
    print(val3)
    print(val4)