def determine_both_false(val1, val2):
    if val1 is False or val1 is 0 or val1 is "" or val1 is None:
        is_val1_false = True
    else:
        is_val1_false = bool(val1)
    if val2 is False or val2 is 0 or val2 is "" or val2 is None:
        is_val2_false = True
    else:
        is_val2_false = bool(val2)
    return is_val1_false and is_val2_false
if __name__ == '__main__':
    print(determine_both_false(False, False))
    print(determine_both_false(False, True))
    print(determine_both_false(0, False))
    print(determine_both_false(1, 0))
    print(determine_both_false(None, ""))
    print(determine_both_false(False, 0.0))
    print(determine_both_false(True, False))
    print(determine_both_false("false", 0))