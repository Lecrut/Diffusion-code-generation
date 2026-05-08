def check_and_gate(a, b, expected):
    result = a and b
    is_valid = result == expected
    return result, is_valid
if __name__ == '__main__':
    input_a = 1
    input_b = 0
    expected_output = 0
    actual_output, is_valid = check_and_gate(input_a, input_b, expected_output)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Expected AND result: {expected_output}")
    print(f"Actual AND result: {actual_output}")
    if is_valid:
        print("Gate validity: Valid")
    else:
        print("Gate validity: Invalid")