def check_both_false(x: bool, y: bool) -> bool:
    if not isinstance(x, bool) or not isinstance(y, bool):
        raise ValueError("Both inputs must be boolean types")
    return not bool(x) and not bool(y)

if __name__ == '__main__':
    print(check_both_false(False, False))
    print(check_both_false(True, False))
    print(check_both_false(False, True))
    print(check_both_false(True, True))