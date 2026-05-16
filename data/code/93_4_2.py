def determine_both_false(val1, val2):
    if val1 is False or val1 is 0 or val1 is "" or val1 is None:
        is_false1 = True
    else:
        is_false1 = bool(val1)
    if val2 is False or val2 is 0 or val2 is "" or val2 is None:
        is_false2 = True
    else:
        is_false2 = bool(val2)
    return is_false1 and is_false2
if __name__ == '__main__':
    print(determine_both_false(False, False))
    print(determine_both_false(False, True))
    print(determine_both_false(0, False))
    print(determine_both_false(1, False))
    print(determine_both_false(False, 0))
    print(determine_both_false(None, False))
    print(determine_both_false(1, 1))
    print(determine_both_false("False", "0"))
    print(determine_both_false(True, False))