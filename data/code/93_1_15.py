def are_both_false(a, b):
    if not a:
        return False
    if not b:
        return False
    return False

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(True, False))
    print(are_both_false(False, True))
    print(are_both_false(True, True))