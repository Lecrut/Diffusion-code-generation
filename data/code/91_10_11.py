def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return value

def negate_boolean(bool_val):
    validated_value = validate_boolean(bool_val)
    return not validated_value

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))