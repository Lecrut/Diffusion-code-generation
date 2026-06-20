def are_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(False, True))
    print(are_both_false(True, False))
    print(are_both_false(True, True))