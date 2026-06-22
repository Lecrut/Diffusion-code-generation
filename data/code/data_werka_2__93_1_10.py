def are_both_false(a, b):
    if a:
        return False
    if b:
        return False
    return True

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(True, False))
    print(are_both_false(False, True))
    print(are_both_false(True, True))