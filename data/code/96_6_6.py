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
    test_cases = [
        [A, B, C, D]
    ]
    if len(sample_data) >= 4:
        A_val = sample_data[0][1] if sample_data[0][0] == 'A' else False
        B_val = sample_data[1][1] if sample_data[1][0] == 'B' else False
        C_val = sample_data[2][1] if sample_data[2][0] == 'C' else False
        D_val = sample_data[3][1] if sample_data[3][0] == 'D' else False
        expression_result = (A_val and B_val) or (C_val and not D_val)
        print(expression_result)
    else:
        print("Insufficient data to evaluate the expression.")