def evaluate_logic_gate(inputs):
    lookup_table = {
        (0, 0, 0): 0,
        (0, 0, 1): 0,
        (0, 1, 0): 0,
        (0, 1, 1): 0,
        (1, 0, 0): 0,
        (1, 0, 1): 0,
        (1, 1, 0): 0,
        (1, 1, 1): 1,
    }
    return lookup_table[inputs]

def validate_gate_output(actual_output, expected_output):
    return actual_output == expected_output

if __name__ == '__main__':
    sample_inputs = (1, 0, 1)
    expected_result = 0
    computed_result = evaluate_logic_gate(sample_inputs)
    is_valid = validate_gate_output(computed_result, expected_result)
    print(f"Inputs: {sample_inputs}")
    print(f"Computed Output: {computed_result}")
    print(f"Expected Output: {expected_result}")
    print(f"Validation Result: {is_valid}")