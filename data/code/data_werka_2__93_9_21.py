def _validate_boolean(value):
    if value is not True and value is not False:
        raise ValueError("Input must be a boolean")
    return value

def check_both_false(a, b):
    validated_a = _validate_boolean(a)
    validated_b = _validate_boolean(b)
    return validated_a is False and validated_b is False

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)