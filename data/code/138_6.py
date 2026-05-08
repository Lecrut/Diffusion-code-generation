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
            if not sub_expr:
                return None
            if 'NOT' in sub_expr:
                parts = sub_expr.split('NOT')
                if len(parts) != 2:
                    raise ValueError("Invalid NOT structure")
                operand = parts[0].strip()
                result = evaluate_sub_expression(operand, inputs_map)
                if result is None:
                    return None
                return not result
            if 'AND' in sub_expr:
                parts = sub_expr.split('AND')
                if len(parts) != 2:
                    raise ValueError("Invalid AND structure")
                left = evaluate_sub_expression(parts[0].strip(), inputs_map)
                right = evaluate_sub_expression(parts[1].strip(), inputs_map)
                if left is None or right is None:
                    return None
                return left and right
            if 'OR' in sub_expr:
                parts = sub_expr.split('OR')
                if len(parts) != 2:
                    raise ValueError("Invalid OR structure")
                left = evaluate_sub_expression(parts[0].strip(), inputs_map)
                right = evaluate_sub_expression(parts[1].strip(), inputs_map)
                if left is None or right is None:
                    return None
                return left or right
            if sub_expr in inputs_map:
                return inputs_map[sub_expr]
            raise ValueError(f"Could not evaluate sub-expression: {sub_expr}")
        try:
            result = evaluate_sub_expression(expression, current_inputs)
            results.append(result)
        except ValueError:
            results.append(None)
    return results
if __name__ == '__main__':
    expression1 = "P AND Q"
    inputs1 = [
        {'P': False, 'Q': False},
        {'P': False, 'Q': True},
        {'P': True, 'Q': False},
        {'P': True, 'Q': True}
    ]
    print("Expression:", expression1)
    print("Inputs:")
    for inputs in inputs1:
        result = evaluate_boolean_expression(expression1, [inputs])
        print(f"Inputs: {inputs} -> Result: {result}")
    print("\n" + "="*20 + "\n")
    expression2 = "(P OR Q) AND NOT P"
    inputs2 = [
        {'P': False, 'Q': False},
        {'P': False, 'Q': True},
        {'P': True, 'Q': False},
        {'P': True, 'Q': True}
    ]
    print("Expression:", expression2)
    print("Inputs:")
    for inputs in inputs2:
        result = evaluate_boolean_expression(expression2, [inputs])
        print(f"Inputs: {inputs} -> Result: {result}")