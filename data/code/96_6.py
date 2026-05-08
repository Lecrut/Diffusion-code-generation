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
    if len(sample_data) >= 4:
        A_val = sample_data[0][1]
        B_val = sample_data[1][1]
        C_val = sample_data[2][1]
        D_val = sample_data[3][1]
        test_result = (A_val and B_val) or (C_val and not D_val)
        print(f"A={A_val}, B={B_val}, C={C_val}, D={D_val}")
        print(f"Result: {test_result}")
    else:
        print("Sample data is insufficient to test the expression (A and B) or (C and not D).")