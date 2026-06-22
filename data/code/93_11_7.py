def both_false(a: bool, b: bool) -> bool:
    FALSE_VALUE = False
    return a is FALSE_VALUE and b is FALSE_VALUE

if __name__ == '__main__':
    print(both_false(False, False))
    print(both_false(True, False))
    print(both_false(False, True))
    print(both_false(True, True))