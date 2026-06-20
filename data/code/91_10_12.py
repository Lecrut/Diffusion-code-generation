def negate_boolean(bool_val):
    return not bool_val
if __name__ == '__main__':
    test_values = {True: False, False: True}
    for input_value, expected_output in test_values.items():
        result = negate_boolean(input_value)
        print(f'Input: {input_value}, Expected Output: {expected_output}, Actual Output: {result}')