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
                    return False
            else:
                return False
        if not sub_results:
            return False
        results.append(any(sub_results))
    return all(results)
if __name__ == '__main__':
    test_expression_1 = "A == 10 & B != 5"
    test_values_1 = {1: 10, 2: 6}
    result_1 = evaluate_boolean_expression(test_expression_1, test_values_1)
    print(f"Expression: {test_expression_1}, Values: {test_values_1}, Result: {result_1}")
    test_expression_2 = "(A == 10 | B != 5) & (C >= 15)"
    test_values_2 = {1: 10, 2: 6, 3: 16}
    result_2 = evaluate_boolean_expression(test_expression_2, test_values_2)
    print(f"Expression: {test_expression_2}, Values: {test_values_2}, Result: {result_2}")
    test_expression_3 = "A == 10 & B == 6"
    test_values_3 = {1: 10, 2: 6}
    result_3 = evaluate_boolean_expression(test_expression_3, test_values_3)
    print(f"Expression: {test_expression_3}, Values: {test_values_3}, Result: {result_3}")
    test_expression_4 = "A == 10 | B != 5 | C < 15"
    test_values_4 = {1: 10, 2: 6, 3: 16}
    result_4 = evaluate_boolean_expression(test_expression_4, test_values_4)
    print(f"Expression: {test_expression_4}, Values: {test_values_4}, Result: {result_4}")
    test_expression_5 = "A == 10 & B == 10"
    test_values_5 = {1: 10, 2: 6}
    result_5 = evaluate_boolean_expression(test_expression_5, test_values_5)
    print(f"Expression: {test_expression_5}, Values: {test_values_5}, Result: {result_5}")
    test_expression_6 = "A == 10 | B != 5"
    test_values_6 = {1: 10, 2: 5}
    result_6 = evaluate_boolean_expression(test_expression_6, test_values_6)
    print(f"Expression: {test_expression_6}, Values: {test_values_6}, Result: {result_6}")