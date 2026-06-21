BOOLEAN_NEGATION_TABLE = {
    True: False,
    False: True,
}

def ensure_boolean(input_data: object) -> bool:
    if not isinstance(input_data, bool):
        raise ValueError("Expected a boolean value")
    return input_data

def negate_boolean(input_data: object) -> bool:
    validated_value = ensure_boolean(input_data)
    return BOOLEAN_NEGATION_TABLE[validated_value]

if __name__ == '__main__':
    test_inputs = [True, False, True, False]
    for inp in test_inputs:
        output = negate_boolean(inp)
        print(output)