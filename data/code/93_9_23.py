def check_both_false(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean")
    return a == False and b == False

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)
    result2 = check_both_false(True, False)
    print(result2)