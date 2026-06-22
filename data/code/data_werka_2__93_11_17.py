def both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    return a is False and b is False

if __name__ == '__main__':
    print(both_false(False, False))
    print(both_false(True, False))
    print(both_false(False, True))
    print(both_false(True, True))