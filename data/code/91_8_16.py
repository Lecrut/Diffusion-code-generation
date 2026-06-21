def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def get_negation(value):
    validated = validate_boolean(value)
    return not validated

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        original = case
        result = get_negation(original)
        print(f"Original: {original}, Negated: {result}")