def check_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return a is False and b is False

if __name__ == '__main__':
    val1 = False
    val2 = False
    result = check_both_false(val1, val2)
    print(result)