AND_GATE = {0: 0, 1: lambda x, y: x * y}

def check_and_gate(a, b):
    expected = AND_GATE[0]
    result = AND_GATE[1](a, b)
    is_valid = result == expected
    return result, is_valid

if __name__ == '__main__':
    input_a = 1
    input_b = 0
    actual_output, is_valid = check_and_gate(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Expected AND result: {expected_output}")
    print(f"Actual AND result: {actual_output}")
    if is_valid:
        print("Gate validity: Valid")
    else:
        print("Gate validity: Invalid")