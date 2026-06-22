BOOL_MAPPING = {'True': 'False', 'False': 'True'}

def get_inverted_boolean_string(input_value: str) -> str:
    if input_value in BOOL_MAPPING:
        return BOOL_MAPPING[input_value]
    raise ValueError(f"Invalid boolean string: {input_value}")

if __name__ == '__main__':
    test_input = 'False'
    result = get_inverted_boolean_string(test_input)
    print(result)