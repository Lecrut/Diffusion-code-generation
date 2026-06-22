def invert_boolean_entry(values):
    if len(values) != 1:
        raise ValueError("Input list must contain exactly one element")
    raw_value = values[0]
    if not isinstance(raw_value, bool):
        raise ValueError("List element must be a boolean")
    negated_value = not raw_value
    return negated_value

if __name__ == '__main__':
    test_data = [False]
    outcome = invert_boolean_entry(test_data)
    print(outcome)