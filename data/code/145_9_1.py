def evaluate_boolean_expression(expression, values):
    tokens = expression.split(' & ')
    results = []
    for token in tokens:
        parts = token.split(' | ')
        sub_results = []
        for part in parts:
            sub_parts = part.split(' == ')
            if len(sub_parts) == 2:
                op = sub_parts[0].strip()
                val1_str = sub_parts[1].strip()
                try:
                    val1 = float(val1_str)
                    val2 = float(values[int(op.split('_')[0])])
                    if op == '==':
                        sub_results.append(val1 == val2)
                    elif op == '!=':
                        sub_results.append(val1 != val2)
                    elif op == '>':
                        sub_results.append(val1 > val2)
                    elif op == '<':
                        sub_results.append(val1 < val2)
                    elif op == '>=':
                        sub_results.append(val1 >= val2)
                    elif op == '<=':
                        sub_results.append(val1 <= val2)
                except ValueError:
                    return None
            else:
                return None
        if sub_results:
            results.append(any(sub_results))
        else:
            results.append(False)
    return any(results)
if __name__ == '__main__':
    test_expression_1 = "A == 10 & B != 5"
    test_values_1 = {1: 10.0, 2: 6.0}
    result_1 = evaluate_boolean_expression(test_expression_1, test_values_1)
    print(f"Expression: {test_expression_1}, Values: {test_values_1}")
    print(f"Result: {result_1}")
    test_expression_2 = "(A == 10 | B != 5) & (C >= 12)"
    test_values_2 = {1: 10.0, 2: 6.0, 3: 12.0}
    result_2 = evaluate_boolean_expression(test_expression_2, test_values_2)
    print(f"Expression: {test_expression_2}, Values: {test_values_2}")
    print(f"Result: {result_2}")
    test_expression_3 = "A == 10 | B == 6"
    test_values_3 = {1: 10.0, 2: 6.0}
    result_3 = evaluate_boolean_expression(test_expression_3, test_values_3)
    print(f"Expression: {test_expression_3}, Values: {test_values_3}")
    print(f"Result: {result_3}")
    test_expression_4 = "A > 10 & B < 5"
    test_values_4 = {1: 10.0, 2: 6.0}
    result_4 = evaluate_boolean_expression(test_expression_4, test_values_4)
    print(f"Expression: {test_expression_4}, Values: {test_values_4}")
    print(f"Result: {result_4}")
    test_expression_5 = "(A == 10 & B != 5) | (C == 12)"
    test_values_5 = {1: 10.0, 2: 6.0, 3: 12.0}
    result_5 = evaluate_boolean_expression(test_expression_5, test_values_5)
    print(f"Expression: {test_expression_5}, Values: {test_values_5}")
    print(f"Result: {result_5}")