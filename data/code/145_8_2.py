def evaluate_boolean_expression(expression, values):
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    values_map = {}
    for i, val in enumerate(values):
        values_map[f'v{i}'] = val
    def evaluate_term(tokens_list):
        if not tokens_list:
            return None, None
        if len(tokens_list) == 1:
            token = tokens_list[0]
            if token in values_map:
                return values_map[token], tokens_list[0]
            else:
                raise NameError(f"Undefined variable or value: {token}")
        if tokens_list[0] in (True, False):
            return tokens_list[0], tokens_list[0]
        if tokens_list[0] == '-':
            if len(tokens_list) < 2:
                raise ValueError("Incomplete unary negation")
            operand_val, operand_token = evaluate_term(tokens_list[1:])
            return not operand_val, operand_token
        if tokens_list[0] == 'NOT':
            if len(tokens_list) < 2:
                raise ValueError("Incomplete NOT operation")
            operand_val, operand_token = evaluate_term(tokens_list[1:])
            return not operand_val, operand_token
        raise NotImplementedError("Complex infix evaluation requires a full Shunting-Yard/RPN implementation, which is too complex for this scope. Using direct evaluation for demonstration.")
    return None, None
def evaluate_nested_booleans(expression, values):
    value_map = {f'v{i}': values[i] for i in range(len(values))}
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    tokens = [t for t in tokens if t]
    values_stack = []
    operators_stack = []
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    def apply_op():
        op = operators_stack.pop()
        if op == 'NOT':
            operand = values_stack.pop()
            values_stack.append(not operand)
        elif op in ('AND', 'OR'):
            right = values_stack.pop()
            left = values_stack.pop()
            if op == 'AND':
                values_stack.append(left and right)
            elif op == 'OR':
                values_stack.append(left or right)
    for token in tokens:
        if token in value_map:
            values_stack.append(value_map[token])
        elif token == '(':
            operators_stack.append(token)
        elif token == ')':
            while operators_stack[-1] != '(':
                apply_op()
            operators_stack.pop()
        elif token in precedence:
            while (operators_stack and operators_stack[-1] != '(' and 
                   precedence.get(operators_stack[-1], 0) >= precedence[token]):
                apply_op()
            operators_stack.append(token)
        else:
            raise ValueError(f"Unknown token: {token}")
    while operators_stack:
        apply_op()
    if len(values_stack) != 1:
        raise ValueError("Invalid expression structure resulting in multiple values on stack.")
    return values_stack[0]
if __name__ == '__main__':
    sample_expression = "(v0 AND v1) OR (NOT v2 AND v3)"
    sample_values = [True, False, True, False]
    try:
        result = evaluate_nested_booleans(sample_expression, sample_values)
        print(f"Expression: {sample_expression}")
        print(f"Values: {sample_values}")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error during evaluation: {e}")
    sample_expression_2 = "NOT (v0 OR v1) AND v2"
    sample_values_2 = [True, True, True]
    try:
        result_2 = evaluate_nested_booleans(sample_expression_2, sample_values_2)
        print(f"\nExpression: {sample_expression_2}")
        print(f"Values: {sample_values_2}")
        print(f"Result: {result_2}")
    except Exception as e:
        print(f"Error during evaluation: {e}")