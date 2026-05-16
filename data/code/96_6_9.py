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
        A_val = case[0][1] if len(case) > 0 else False
        B_val = case[1][1] if len(case) > 1 else False
        C_val = case[2][1] if len(case) > 2 else False
        D_val = case[3][1] if len(case) > 3 else False
        def evaluate_specific(var_list):
            if len(var_list) < 4:
                return []
            A = var_list[0][1]
            B = var_list[1][1]
            C = var_list[2][1]
            D = var_list[3][1]
            result = (A and B) or (C and not D)
            return [result]
        def evaluate_expression_final(variables):
            if len(variables) < 4:
                return []
            A = variables[0][1]
            B = variables[1][1]
            C = variables[2][1]
            D = variables[3][1]
            result = (A and B) or (C and not D)
            return [result]
        result1 = evaluate_expression_final(test_cases[0])
        print(f"Test Case 1 Result: {result1}")
        assert result1[0] == True
        result2 = evaluate_expression_final(test_cases[1])
        print(f"Test Case 2 Result: {result2}")
        assert result2[0] == True
        result3 = evaluate_expression_final(test_cases[2])
        print(f"Test Case 3 Result: {result3}")
        assert result3[0] == True