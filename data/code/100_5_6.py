def check_logic_consistency(input_a, input_b):
    expected_output = input_a and input_b
    return expected_output

if __name__ == '__main__':
    result = check_logic_consistency(True, False)
    print(result)