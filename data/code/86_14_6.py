def are_booleans_equal(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    print(are_booleans_equal(True, True))
    print(are_booleans_equal(False, False))
    print(are_booleans_equal(True, False))