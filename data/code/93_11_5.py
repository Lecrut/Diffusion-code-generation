def both_false(a: bool, b: bool) -> bool:
    if a:
        return False
    if b:
        return False
    return True

if __name__ == '__main__':
    print(both_false(False, False))
    print(both_false(True, False))
    print(both_false(False, True))
    print(both_false(True, True))