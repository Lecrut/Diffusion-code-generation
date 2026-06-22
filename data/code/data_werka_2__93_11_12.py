TRUE_VAL = True
FALSE_VAL = False

def both_false(a: bool, b: bool) -> bool:
    return a is FALSE_VAL and b is FALSE_VAL

if __name__ == '__main__':
    print(both_false(False, False))
    print(both_false(True, False))
    print(both_false(False, True))
    print(both_false(True, True))