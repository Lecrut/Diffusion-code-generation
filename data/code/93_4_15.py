def determine_both_false(val1, val2):
    return not bool(val1) and not bool(val2)

if __name__ == '__main__':
    print(determine_both_false(0, ''))
    print(determine_both_false(None, False))
    print(determine_both_false([], {}))