def fast_bool_compare(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values")
    return a == b

if __name__ == '__main__':
    print(fast_bool_compare(True, True))
    print(fast_bool_compare(False, False))
    print(fast_bool_compare(True, False))