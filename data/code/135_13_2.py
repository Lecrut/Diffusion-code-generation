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
                val1 = evaluate_expression(operand1, context)
                if val1 is None:
                    return None
                return not val1
            elif len(parts) == 1:
                operand = parts[0]
                val = evaluate_expression(operand, context)
                if val is None:
                    return None
                return not val
        try:
            if expression == 'True':
                return True
            if expression == 'False':
                return False
            if expression == 'True': return True
            if expression == 'False': return False
            return None
        except Exception:
            return None
    if isinstance(expression, bool):
        return expression
    return None
def safe_evaluate(expression):
    return evaluate_expression(expression)
if __name__ == '__main__':
    expression1 = "True and not False"
    expression2 = "True"
    result1 = safe_evaluate(expression1)
    result2 = safe_evaluate(expression2)
    print(f"Expression 1: {expression1}, Result: {result1}")
    print(f"Expression 2: {expression2}, Result: {result2}")
    if result1 == result2:
        print("The two expressions evaluate to the same truth value.")
    else:
        print("The two expressions evaluate to different truth values.")