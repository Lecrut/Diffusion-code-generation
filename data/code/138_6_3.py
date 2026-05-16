def evaluate_boolean_expression(expression, inputs):
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
    num_vars = len(var_list)
    results = []
    for i in range(2**num_vars):
        current_inputs = {}
        for j in range(num_vars):
            current_inputs[var_list[j]] = bool((i >> j) & 1)
        substitutions = {}
        for var in var_list:
            substitutions[var] = current_inputs[var]
        def evaluate_sub_expression(expr, values):
            if 'NOT' in expr:
                op, arg = expr.split()
                return not evaluate_sub_expression(arg, values)
            if len(expr.split()) == 1:
                return values.get(expr.split()[0], False)
            parts = expr.split()
            if len(parts) == 3 and parts[1] in ['AND', 'OR']:
                left_val = evaluate_sub_expression(parts[0], values)
                right_val = evaluate_sub_expression(parts[2], values)
                if parts[1] == 'AND':
                    return left_val and right_val
                elif parts[1] == 'OR':
                    return left_val or right_val
            return None
        try:
            result = evaluate_sub_expression(expression, substitutions)
            results.append(result)
        except Exception:
            results.append(None)
    return results
if __name__ == '__main__':
    expression = 'P AND Q'
    inputs = [
        {'P': False, 'Q': False},
        {'P': False, 'Q': True},
        {'P': True, 'Q': False},
        {'P': True, 'Q': True}
    ]
    results = []
    for input_set in inputs:
        try:
            result = evaluate_boolean_expression(expression, [input_set['P'], input_set['Q']])
            results.append(result)
        except Exception:
            results.append(None)
    print(results)