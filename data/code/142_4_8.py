def validate_boolean_equality(bool1: bool, bool2: bool) -> bool:
    return bool1 ^ bool2

if __name__ == '__main__':
    result = validate_boolean_equality(True, False)
    print(result)