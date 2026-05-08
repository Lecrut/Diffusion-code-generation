def evaluate_expressions(variables):
    results = []
    for var_tuple in variables:
        A, B = var_tuple[0], var_tuple[1]
        C, D = var_tuple[2], var_tuple[3]
        expression_result = (A and B) or (C and not D)
        results.append(expression_result)
    return results
if __name__ == '__main__':
    test_data = [
        ('A', True, 'B', False),
        ('A', False, 'B', True),
        ('A', True, 'B', True),
        ('A', False, 'B', False)
    ]
    evaluated_results = evaluate_expressions(test_data)
    print(evaluated_results)