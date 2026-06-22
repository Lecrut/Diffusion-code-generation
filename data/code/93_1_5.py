def are_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean types")
    return a is False and b is False

if __name__ == '__main__':
    val1 = are_both_false(False, False)
    print(val1)
    val2 = are_both_false(True, False)
    print(val2)
    val3 = are_both_false(False, True)
    print(val3)
    val4 = are_both_false(True, True)
    print(val4)