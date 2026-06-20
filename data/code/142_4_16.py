def validate_boolean_equality(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    
    return a ^ b

if __name__ == '__main__':
    print(validate_boolean_equality(True, False))
    print(validate_boolean_equality(True, True))
    print(validate_boolean_equality(False, False))
    print(validate_boolean_equality(True, True))
    print(validate_boolean_equality(False, True))