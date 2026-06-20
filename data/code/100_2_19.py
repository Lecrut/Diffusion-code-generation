def and_gate(a, b):
    return a and b

def check_and_gate(result, expected):
    is_valid = result == expected
    return is_valid

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    expected_output = 0
    actual_output = and_gate(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Expected AND result: {expected_output}")
    print(f"Actual AND result: {actual_output}")
    if check_and_gate(actual_output, expected_output):
        print("Gate validity: Valid")
    else:
        print("Gate validity: Invalid")