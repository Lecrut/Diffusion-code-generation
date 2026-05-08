import ast
def evaluate_expression(expression, context):
    if expression == 'True':
        return True
    if expression == 'False':
        return False
    if isinstance(expression, str):
        parts = expression.split()
        if len(parts) == 3:
            op = parts[1]
            left_val = evaluate_expression(parts[0], context)
            right_val = evaluate_expression(parts[2], context)
            if op == 'and':
                return left_val and right_val
            elif op == 'or':
                return left_val or right_val
            elif op == 'not':
                return not left_val
    if isinstance(expression, bool):
        return expression
    raise ValueError(f"Could not evaluate expression: {expression}")
def safe_eval(expression):
    try:
        if expression == 'True':
            return True
        if expression == 'False':
            return False
        if expression.lower() in ('true', 'false'):
            return expression.lower() == 'true'
        if expression == 'True':
            return True
        if expression == 'False':
            return False
        if expression == 'True':
            return True
        if expression == 'False':
            return False
        if expression.lower() == 'true':
            return True
        if expression.lower() == 'false':
            return False
        raise ValueError("Unsupported expression format for safe evaluation.")
    except Exception:
        raise ValueError(f"Error during safe evaluation of '{expression}'")
def solve():
    expression1 = 'True'
    expression2 = 'True'
    expression1 = 'True'
    expression2 = 'False'
    try:
        val1 = safe_eval(expression1)
        val2 = safe_eval(expression2)
        if val1 == val2:
            print("The two expressions evaluate to the same truth value.")
        else:
            print("The two expressions evaluate to different truth values.")
    except ValueError as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    solve()