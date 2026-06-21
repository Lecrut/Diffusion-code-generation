def are_equivalent(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    print(are_equivalent(True, True))
    print(are_equivalent(True, False))
    print(are_equivalent(False, True))
    print(are_equivalent(False, False))