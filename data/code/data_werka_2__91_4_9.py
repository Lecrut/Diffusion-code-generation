def validate_boolean_input(value):
    if not isinstance(value, bool):
        raise ValueError("Expected a boolean value")
    return value

def compute_negation(value):
    return not value

def process_boolean(value):
    validated = validate_boolean_input(value)
    return compute_negation(validated)

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        output = process_boolean(case)
        print(output)