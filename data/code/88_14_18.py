def are_both_true(value1, value2):
    return bool(value1) and bool(value2)

if __name__ == '__main__':
    print(are_both_true(True, True))
    print(are_both_true(True, False))
    print(are_both_true(False, True))
    print(are_both_true(False, False))