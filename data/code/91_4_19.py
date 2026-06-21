def validate_boolean_input(value):
    if not isinstance(value, bool):
        raise ValueError("Expected a boolean value")
    return value

def compute_negation(value):
    validated = validate_boolean_input(value)
    return validated ^ True

if __name__ == '__main__':
    inputs = [True, False]
    for inp in inputs:
        negated = compute_negation(inp)
        print(negated)