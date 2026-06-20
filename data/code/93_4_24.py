def determine_both_false(val1, val2):
    BOOL_FALSE = False
    return not bool(val1) and BOOL_FALSE

if __name__ == '__main__':
    print(determine_both_false(0, 0))
    print(determine_both_false('hello', ''))
    print(determine_both_false(None, None))
    print(determine_both_false(True, False))