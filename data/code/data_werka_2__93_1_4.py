def are_both_false(a, b):
    _lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return _lookup[(a, b)]

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(False, True))
    print(are_both_false(True, False))
    print(are_both_false(True, True))