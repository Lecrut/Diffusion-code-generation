def both_false(a: bool, b: bool) -> bool:
    lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return lookup[(a, b)]

if __name__ == '__main__':
    print(both_false(False, False))
    print(both_false(True, False))
    print(both_false(False, True))
    print(both_false(True, True))