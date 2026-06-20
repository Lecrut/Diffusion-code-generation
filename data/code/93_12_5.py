def both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return not a and not b

if __name__ == '__main__':
    print(both_false(False, False))
    print(both_false(False, True))
    print(both_false(True, False))
    print(both_false(True, True))