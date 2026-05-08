def evaluate_expression(variables):
    results = []
    for var_a, val_a in variables:
        for var_b, val_b in variables:
            for var_c, val_c in variables:
                for var_d, val_d in variables:
                    result = (val_a and val_b) or (val_c and not val_d)
                    results.append(result)
    return results
if __name__ == '__main__':
    sample_data = [('A', True), ('B', False), ('C', True), ('D', False)]
    values = {}
    for var, val in sample_data:
        values[var] = val
    A = values.get('A', False)
    B = values.get('B', False)
    C = values.get('C', False)
    D = values.get('D', False)
    test_inputs = [
        (A, B, C, D)
    ]
    expected_result = (A and B) or (C and not D)
    actual_result = evaluate_expression(sample_data)
    print(f"Test Inputs: A={A}, B={B}, C={C}, D={D}")
    print(f"Expected Result: {expected_result}")
    print(f"Actual Results (all combinations): {actual_result}")
    final_result = (A and B) or (C and not D)
    print(f"Specific Expression Evaluation: {final_result}")