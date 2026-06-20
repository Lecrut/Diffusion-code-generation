def are_both_false(x, y):
    return not x and (not y)
if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(True, False))
    print(are_both_false(False, True))
    print(are_both_false(True, True))