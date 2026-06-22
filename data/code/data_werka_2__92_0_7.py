def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError(f"Expected bool, got {type(value).__name__}")
    return True

def get_logical_opposite(value):
    validate_boolean(value)
    return value is False

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        result = get_logical_opposite(val)
        print(result)