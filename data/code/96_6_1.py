def evaluate_expression(variables):
    results = []
    for var_a, var_b in variables:
        results.append((var_a and var_b) or (variables[2].get(0, False) and not variables[3].get(0, False)))
    return results
if __name__ == '__main__':
    test_cases = [
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('X', True), ('Y', True), ('Z', False), ('W', True)],
        [('P', False), ('Q', False), ('R', True), ('S', False)]
    ]
    for case in test_cases:
        variables = [tuple(case[i]) for i in range(4)]
        def evaluate_expression_corrected(variables_list):
            results = []
            for item in variables_list:
                if len(item) >= 4:
                    A, B, C, D = item[0], item[1], item[2], item[3]
                    result = (A and B) or (C and not D)
                    results.append(result)
                else:
                    results.append(None)
            return results
        results = evaluate_expression_corrected(variables)
        print(results)