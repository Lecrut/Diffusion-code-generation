def flip_bool_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_values = {True: False, False: True}
    for input_val, expected_output in test_values.items():
        result = flip_bool_value(input_val)
        print(f"Flipping {input_val}: {result}, Expected: {expected_output}")