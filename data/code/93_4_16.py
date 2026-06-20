def determine_both_false(val1, val2):
    return not bool(val1) and (not bool(val2))
if __name__ == '__main__':
    print(determine_both_false(0, 0))
    print(determine_both_false(0, 1))
    print(determine_both_false(1, 0))
    print(determine_both_false(1, 1))
    print(determine_both_false('hello', ''))
    print(determine_both_false(None, None))