def validate_boolean_equality(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    result = validate_boolean_equality(True, False)
    print(result)