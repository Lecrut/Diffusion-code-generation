def check_logic_consistency(input_a, input_b):
    if not isinstance(input_a, bool) or not isinstance(input_b, bool):
        raise ValueError("Inputs must be boolean values")
    expected_output = input_a and input_b
    return expected_output

if __name__ == '__main__':
    result = check_logic_consistency(True, False)
    print(result)