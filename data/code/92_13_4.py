def get_opposite_boolean_string(bool_string):
    lower_string = bool_string.lower()
    if lower_string == 'true':
        return 'False'
    elif lower_string == 'false':
        return 'True'
    else:
        raise ValueError("Invalid boolean string provided")
if __name__ == '__main__':
    test_cases = [
        ('True', 'False'),
        ('false', 'True'),
        ('TRUE', 'False'),
        ('fAlSe', 'True'),
        ('true', 'False'),
        ('FALSE', 'True')
    ]
    for input_str, expected_output in test_cases:
        actual_output = get_opposite_boolean_string(input_str)
        assert actual_output == expected_output, f"Input: {input_str}, Expected: {expected_output}, Got: {actual_output}"
        print(f"Input: {input_str} -> Output: {actual_output}")
    try:
        get_opposite_boolean_string('maybe')
    except ValueError as e:
        print(f"Caught expected error for invalid input: {e}")