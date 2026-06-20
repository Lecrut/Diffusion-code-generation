def validate_booleans(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def check_equivalence(a: bool, b: bool) -> str:
    validate_booleans(a, b)
    return 'Equal' if a == b else 'One is True, the other is False'

if __name__ == '__main__':
    print(check_equivalence(True, True))
    print(check_equivalence(True, False))
    print(check_equivalence(False, True))
    print(check_equivalence(False, False))