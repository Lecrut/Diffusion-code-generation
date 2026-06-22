def verify_both_false(first, second):
    if not isinstance(first, bool):
        raise ValueError("first must be a boolean")
    if not isinstance(second, bool):
        raise ValueError("second must be a boolean")
    return not first and not second

if __name__ == '__main__':
    val1 = False
    val2 = False
    outcome = verify_both_false(val1, val2)
    print(outcome)