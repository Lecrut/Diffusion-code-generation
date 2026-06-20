def are_both_false(A, B):
    return not A and (not B)
if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(True, False))
    print(are_both_false(False, True))
    print(are_both_false(True, True))