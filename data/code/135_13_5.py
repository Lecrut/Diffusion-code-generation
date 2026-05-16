import ast
def evaluate_expression(expression, context=None):
    if context is None:
        context = {}
    if isinstance(expression, str):
        expression = expression.strip()
        if expression.lower() == 'true':
            return True
        if expression.lower() == 'false':
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
                val1 = evaluate_expression(operand1, context)
                if not evaluate_expression(operand2, context):
                    return not val1
                else:
                    return val1
            elif len(parts) == 1:
                operand = parts[0]
                return not evaluate_expression(operand, context)
        if expression.lower() == 'true':
            return True
        if expression.lower() == 'false':
            return False
        raise ValueError(f"Could not evaluate expression: {expression}")
    if isinstance(expression, bool):
        return expression
    if isinstance(expression, ast.Expression):
        node = expression.body
        return evaluate_expression(node, context)
    if isinstance(expression, ast.BoolOp):
        op = expression.op
        values = []
        for item in expression.values:
            values.append(evaluate_expression(item, context))
        if op == 'and':
            return all(values)
        elif op == 'or':
            return any(values)
    if isinstance(expression, ast.UnaryOp):
        op = expression.op
        operand = evaluate_expression(expression.operand, context)
        if op == 'not':
            return not operand
    if isinstance(expression, ast.Constant):
        return expression.value
    raise TypeError(f"Unsupported expression type: {type(expression)}")
def safe_eval(expression_str):
    try:
        processed_str = expression_str.replace(' and ', ' and ')
        processed_str = processed_str.replace(' or ', ' or ')
        processed_str = processed_str.replace(' not ', ' not ')
        return evaluate_expression(expression_str)
    except Exception as e:
        raise ValueError(f"Error during safe evaluation of '{expression_str}': {e}")
if __name__ == '__main__':
    expression1 = "True and not False"
    expression2 = "True"
    try:
        val1 = safe_eval(expression1)
        val2 = safe_eval(expression2)
        if val1 == val2:
            print("The two expressions evaluate to the same truth value.")
        else:
            print("The two expressions evaluate to different truth values.")
    except ValueError as e:
        print(f"An error occurred: {e}")