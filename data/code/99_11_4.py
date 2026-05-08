def evaluate_boolean_expression(expression, variables):
    import re
    def evaluate_token(token, vars):
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            return float(token)
        if token in vars:
            return vars[token]
        raise NameError(f"Variable or undefined token: {token}")
    def parse_and_bind(tokens, vars):
        output_queue = []
        operator_stack = []
        values_stack = []
        precedence = {
            '==': 1, '!=': 1, '>': 2, '<': 2, '>=': 2, '<=': 2,
            'and': 3, 'or': 4, 'not': 5
        }
        def apply_op(op, values):
            if op == 'not':
                if len(values) < 1:
                    raise SyntaxError("Not enough operands for 'not'")
                operand = values.pop()
                result = not evaluate_token(operand, vars)
                values.append(result)
            elif op in ('and', 'or'):
                if len(values) < 2:
                    raise SyntaxError(f"Not enough operands for '{op}'")
                right = values.pop()
                left = values.pop()
                if op == 'and':
                    result = left and right
                else:
                    result = left or right
                values.append(result)
            elif op in ('==', '!=', '>', '<', '>=', '<='):
                if len(values) < 2:
                    raise SyntaxError(f"Not enough operands for comparison operator '{op}'")
                right = values.pop()
                left = values.pop()
                if op == '==': result = left == right
                elif op == '!=': result = left != right
                elif op == '>': result = left > right
                elif op == '<': result = left < right
                elif op == '>=': result = left >= right
                elif op == '<=': result = left <= right
                values.append(result)
            else:
                raise ValueError(f"Unknown operator: {op}")
        for token in tokens:
            if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
                values_stack.append(evaluate_token(token, vars))
            elif token in precedence:
                while (operator_stack and precedence.get(operator_stack[-1], 0) >= precedence[token]):
                    op = operator_stack.pop()
                    apply_op(op, values_stack)
                operator_stack.append(token)
            else:
                raise SyntaxError(f"Invalid token: {token}")
        while operator_stack:
            op = operator_stack.pop()
            if op == 'not':
                if len(values_stack) < 1:
                    raise SyntaxError("Not enough operands for 'not'")
                operand = values_stack.pop()
                result = not evaluate_token(operand, vars)
                values_stack.append(result)
            elif op in ('and', 'or'):
                if len(values_stack) < 2:
                    raise SyntaxError(f"Not enough operands for '{op}'")
                right = values_stack.pop()
                left = values_stack.pop()
                if op == 'and':
                    result = left and right
                else:
                    result = left or right
                values_stack.append(result)
            elif op in ('==', '!=', '>', '<', '>=', '<='):
                if len(values_stack) < 2:
                    raise SyntaxError(f"Not enough operands for comparison operator '{op}'")
                right = values_stack.pop()
                left = values_stack.pop()
                if op == '==': result = left == right
                elif op == '!=': result = left != right
                elif op == '>': result = left > right
                elif op == '<': result = left < right
                elif op == '>=': result = left >= right
                elif op == '<=': result = left <= right
                values_stack.append(result)
            else:
                raise ValueError(f"Internal error processing operator: {op}")
        if len(values_stack) != 1:
            raise SyntaxError("Malformed expression resulting in incorrect stack size")
        return values_stack[0]
    tokens = re.findall(r'[\d\.\-]+|\b(and|or|not|==|!=|>=|<=|>|<)\b', expression)
    variables = {}
    for var, val in variables.items():
        variables[var] = val
    try:
        result = parse_and_bind(tokens, variables)
        return result
    except (SyntaxError, NameError, ValueError) as e:
        raise ValueError(f"Error evaluating expression: {e}")
if __name__ == '__main__':
    test_cases = [
        ("x > 5 and y == 10", {"x": 6, "y": 10}),
        ("not (x == 5)", {"x": 5}),
        ("a > 10 or b < 5", {"a": 12, "b": 3}),
        ("x >= 5 and y <= 10", {"x": 5, "y": 10}),
        ("not (x == 5 and y == 10)", {"x": 5, "y": 10}),
        ("10 > 5 and 2 == 2", {}),
        ("x == 5 or y == 10", {"x": 4, "y": 11}),
        ("x > 10 and not y", {"x": 15, "y": 5}),
        ("10 > 20", {}),
        ("x == 5 and y > 10", {"x": 5, "y": 11}),
        ("x == 5", {"x": 5}),
        ("x == 5 or y == 10 and z == 1", {"x": 5, "y": 10, "z": 1}),
        ("x > 5 and not (y == 10)", {"x": 6, "y": 10}),
        ("10 > 20 and", {}),
        ("x > 5 and", {"x": 6}),
        ("x > 5 and y", {"x": 6, "y": 10}),
        ("x > 5 and y == 10 and z > 1", {"x": 6, "y": 10, "z": 2}),
    ]
    for expression, vars_input in test_cases:
        try:
            result = evaluate_boolean_expression(expression, vars_input)
            print(f"Expression: '{expression}' with variables {vars_input}: Result = {result}")
        except ValueError as e:
            print(f"Expression: '{expression}' with variables {vars_input}: Error = {e}")
        except Exception as e:
            print(f"Expression: '{expression}' with variables {vars_input}: Unexpected Error = {e}")
        print("-" * 20)