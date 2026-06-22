def validate_boolean(input_value):
    if not isinstance(input_value, bool):
        raise ValueError("Input must be a boolean type")
    return input_value

def compute_negation(value):
    is_valid = validate_boolean(value)
    return not is_valid

def generate_negation_report(input_val):
    original = validate_boolean(input_val)
    result = compute_negation(original)
    return {
        "original": original,
        "negated": result
    }

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        report = generate_negation_report(case)
        print(report)