import ast
def evaluate_expression(expression, context=None):
    if context is None:
        context = {}
    if isinstance(expression, str):
        expression = expression.strip()
    if expression == 'True':
        return True
    if expression == 'False':
        return False
    if 'and' in expression:
        parts = [p.strip() for p in expression.split('and')]
        result = True
        for part in parts:
            if not evaluate_expression(part, context):
                result = False
                break
        return result
    if 'or' in expression:
        parts = [p.strip() for p in expression.split('or')]
        result = False
        for part in parts:
            if evaluate_expression(part, context):
                result = True
                break
        return result
    if 'not' in expression:
        parts = [p.strip() for p in expression.split('not')]
        if len(parts) == 2:
            operand1 = parts[0]
            operand2 = parts[1]
            if operand1 == 'True':
                return not evaluate_expression(operand2, context)
            elif operand1 == 'False':
                return not evaluate_expression(operand2, context)
            else:
                raise ValueError("Invalid structure for 'not'")
        else:
            raise ValueError("Invalid structure for 'not'")
    try:
        node = ast.parse(expression, mode='eval')
        return bool(eval(compile(node, filename='<string>', mode='eval'), context))
    except Exception:
        raise ValueError(f"Could not evaluate expression: {expression}")
def compare_boolean_expressions(expr1, expr2):
    try:
        val1 = evaluate_expression(expr1)
        val2 = evaluate_expression(expr2)
        return val1 == val2
    except ValueError:
        return False
if __name__ == '__main__':
    expression1 = "True and not False"
    expression2 = "True"
    result = compare_boolean_expressions(expression1, expression2)
    print(result)