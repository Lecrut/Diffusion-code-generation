def are_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return a is False and b is False

if __name__ == '__main__':
    result = are_both_false(False, False)
    print(result)
    result2 = are_both_false(True, False)
    print(result2)
    result3 = are_both_false(False, True)
    print(result3)
    result4 = are_both_false(True, True)
    print(result4)