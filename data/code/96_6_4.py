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
    n = len(sample_data)
    all_results = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    A_tuple = sample_data[i]
                    B_tuple = sample_data[j]
                    C_tuple = sample_data[k]
                    D_tuple = sample_data[l]
                    A = A_tuple[0]
                    B = B_tuple[0]
                    C = C_tuple[0]
                    D = D_tuple[0]
                    result = (A and B) or (C and not D)
                    all_results.append(result)
    print(all_results)