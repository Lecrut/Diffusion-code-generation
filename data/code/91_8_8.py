TRUE_VALUE = True
FALSE_VALUE = False

def compute_negation(input_value):
    if not isinstance(input_value, bool):
        raise ValueError("Input must be a boolean")
    return not input_value

def display_negation_results(original_value):
    negated_value = compute_negation(original_value)
    print(f"Original: {original_value}")
    print(f"Negated: {negated_value}")

if __name__ == '__main__':
    display_negation_results(TRUE_VALUE)
    display_negation_results(FALSE_VALUE)