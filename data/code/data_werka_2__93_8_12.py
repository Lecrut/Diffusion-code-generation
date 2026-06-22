def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def check_both_false(a, b):
    is_a_valid = validate_boolean(a)
    is_b_valid = validate_boolean(b)
    return not is_a_valid and not is_b_valid

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    outcome = check_both_false(sample_a, sample_b)
    print(outcome)