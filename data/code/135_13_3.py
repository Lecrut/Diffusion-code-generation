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
            if expression.lower() == 'true':
                return True
            if expression.lower() == 'false':
                return False
            return None
        except Exception:
            return None
    if isinstance(expression, bool):
        return expression
    return None
def safe_eval(expression):
    if expression == 'True':
        return True
    if expression == 'False':
        return False
    if isinstance(expression, bool):
        return expression
    if 'and' in expression:
        parts = [p.strip() for p in expression.split('and')]
        result = True
        for part in parts:
            if not evaluate_expression(part):
                result = False
                break
        return result
    if 'or' in expression:
        parts = [p.strip() for p in expression.split('or')]
        result = False
        for part in parts:
            if evaluate_expression(part):
                result = True
                break
        return result
    if 'not' in expression:
        parts = [p.strip() for p in expression.split('not')]
        if len(parts) == 2:
            operand1 = parts[0]
            operand2 = parts[1]
            val1 = evaluate_expression(operand1)
            if val1 is not None:
                return not val1
        elif len(parts) == 1:
            operand = parts[0]
            val = evaluate_expression(operand)
            if val is not None:
                return not val
    return None
if __name__ == '__main__':
    expression1 = "True and False"
    expression2 = "True"
    result1 = evaluate_expression(expression1)
    result2 = evaluate_expression(expression2)
    print(f"Expression 1: {expression1} evaluates to {result1}")
    print(f"Expression 2: {expression2} evaluates to {result2}")
    if result1 == result2:
        print("The two expressions evaluate to the same truth value.")
    else:
        print("The two expressions evaluate to different truth values.")