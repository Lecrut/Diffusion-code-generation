def _validate_boolean_input(value):
    if not isinstance(value, bool):
        raise ValueError("Expected a boolean value")
    return value

def negate_boolean(value):
    _validate_boolean_input(value)
    return not value

if __name__ == '__main__':
    true_result = negate_boolean(True)
    false_result = negate_boolean(False)
    print(true_result)
    print(false_result)