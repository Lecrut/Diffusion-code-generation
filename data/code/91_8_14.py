def validate_and_negate(boolean_input):
    if not isinstance(boolean_input, bool):
        raise ValueError("Input must be a boolean")
    return not boolean_input

def demonstrate_negation():
    test_cases = [True, False]
    for val in test_cases:
        original = val
        result = validate_and_negate(val)
        print(f"Input: {original}, Result: {result}")

if __name__ == '__main__':
    demonstrate_negation()