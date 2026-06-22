def apply_negation(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

NEGATION_MAP = {
    True: False,
    False: True
}

def get_negated_value(value):
    return NEGATION_MAP.get(value, apply_negation(value))

if __name__ == '__main__':
    test_cases = [True, False]
    for original in test_cases:
        result = get_negated_value(original)
        print(f"Original: {original}, Negated: {result}")