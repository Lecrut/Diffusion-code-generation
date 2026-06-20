def validate_boolean_equality(a: bool, b: bool) -> bool:
    return a ^ b
if __name__ == '__main__':
    print(validate_boolean_equality(True, False))
    print(validate_boolean_equality(False, False))