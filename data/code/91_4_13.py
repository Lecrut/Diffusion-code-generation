def validate_boolean_input(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean type")
    return value

def compute_negation(value):
    validated = validate_boolean_input(value)
    return not validated

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        output = compute_negation(case)
        print(output)