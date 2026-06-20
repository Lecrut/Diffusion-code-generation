def validate_input(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def are_booleans_identical(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return a == b

if __name__ == '__main__':
    print(are_booleans_identical(True, True))
    print(are_booleans_identical(False, False))
    print(are_booleans_identical(True, False))