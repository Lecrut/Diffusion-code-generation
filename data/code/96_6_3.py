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
    values = {name: value for name, value in sample_data}
    A = next(val for name, val in sample_data if name == 'A')
    B = next(val for name, val in sample_data if name == 'B')
    C = next(val for name, val in sample_data if name == 'C')
    D = next(val for name, val in sample_data if name == 'D')
    test_result = (A and B) or (C and not D)
    print(test_result)