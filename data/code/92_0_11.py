BOOLEAN_FALSE = False
BOOLEAN_TRUE = True

def validate_boolean(input_data):
    if not isinstance(input_data, bool):
        raise ValueError("Input must be a boolean type")
    return input_data

def get_logical_opposite(value):
    validated_value = validate_boolean(value)
    return not validated_value

if __name__ == '__main__':
    test_values = [BOOLEAN_TRUE, BOOLEAN_FALSE]
    for val in test_values:
        result = get_logical_opposite(val)
        print(result)