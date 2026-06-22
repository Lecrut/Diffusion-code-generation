def _ensure_boolean(value: object) -> bool:
    if isinstance(value, bool):
        return value
    raise ValueError("Input must be a boolean type")

def negate_boolean(value: object) -> bool:
    raw_value = _ensure_boolean(value)
    inverted_state = not raw_value
    return inverted_state

if __name__ == '__main__':
    sample_input_one = True
    sample_input_two = False
    
    outcome_one = negate_boolean(sample_input_one)
    outcome_two = negate_boolean(sample_input_two)
    
    print(outcome_one)
    print(outcome_two)