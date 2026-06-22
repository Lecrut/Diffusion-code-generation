def check_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return not (a or b)

if __name__ == '__main__':
    val1 = False
    val2 = False
    result = check_both_false(val1, val2)
    print(result)
    val3 = True
    val4 = False
    result2 = check_both_false(val3, val4)
    print(result2)