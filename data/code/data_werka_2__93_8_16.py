def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")
    return value

def check_both_false(a, b):
    validated_a = validate_boolean(a)
    validated_b = validate_boolean(b)
    return validated_a is False and validated_b is False

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    outcome = check_both_false(sample_a, sample_b)
    print(outcome)