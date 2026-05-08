def evaluate_boolean_expression(expression, inputs):
    if not expression:
        return None
    tokens = expression.upper().split()
    variables = set()
    operators = []
    for token in tokens:
        if token in ['AND', 'OR', 'NOT']:
            operators.append(token)
        else:
            variables.add(token)
    if not variables:
        return None
    var_list = sorted(list(variables))
    n = len(var_list)
    results = []
    for i in range(2**n):
        current_inputs = {}
        temp_i = i
        for j in range(n):
            current_inputs[var_list[j]] = bool((temp_i >> j) & 1)
        def evaluate_sub_expression(sub_expr, inputs_map):
            if 'NOT' in sub_expr:
                parts = sub_expr.split('NOT')
                operand = parts[0].strip()
                return not evaluate_sub_expression(operand, inputs_map)
            if 'AND' in sub_expr:
                parts = sub_expr.split('AND')
                results_and = [evaluate_sub_expression(p, inputs_map) for p in parts]
                return all(results_and)
            if 'OR' in sub_expr:
                parts = sub_expr.split('OR')
                results_or = [evaluate_sub_expression(p, inputs_map) for p in parts]
                return any(results_or)
            if 'NOT' in sub_expr:
                if sub_expr == var_list[0] or sub_expr == var_list[1] or sub_expr == var_list[2]:
                    return inputs_map.get(sub_expr, False)
                return False
            return inputs_map.get(sub_expr, False)
        try:
            result = evaluate_sub_expression(expression, current_inputs)
            results.append(result)
        except Exception:
            results.append(None)
    return results
if __name__ == '__main__':
    expression = 'P AND Q'
    sample_inputs = [
        {'P': False, 'Q': False},
        {'P': False, 'Q': True},
        {'P': True, 'Q': False},
        {'P': True, 'Q': True}
    ]
    print(f"Expression: {expression}")
    print("Inputs:")
    for inputs in sample_inputs:
        result = evaluate_boolean_expression(expression, [inputs['P'], inputs['Q']])
        print(f"Inputs P={inputs['P']}, Q={inputs['Q']}: Result={result}")
    print("\n--- Another Example: (P OR Q) AND NOT R ---")
    expression2 = '(P OR Q) AND NOT R'
    sample_inputs2 = [
        {'P': False, 'Q': False, 'R': False},
        {'P': False, 'Q': False, 'R': True},
        {'P': False, 'Q': True, 'R': False},
        {'P': False, 'Q': True, 'R': True},
        {'P': True, 'Q': False, 'R': False},
        {'P': True, 'Q': False, 'R': True},
        {'P': True, 'Q': True, 'R': False},
        {'P': True, 'Q': True, 'R': True}
    ]
    print(f"Expression: {expression2}")
    print("Inputs:")
    for inputs in sample_inputs2:
        result = evaluate_boolean_expression(expression2, [inputs['P'], inputs['Q'], inputs['R']])
        print(f"Inputs P={inputs['P']}, Q={inputs['Q']}, R={inputs['R']}: Result={result}")