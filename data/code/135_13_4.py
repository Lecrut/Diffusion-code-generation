import ast
def evaluate_expression(expression, context=None):
    if context is None:
        context = {}
    if isinstance(expression, str):
        expression = expression.strip()
        if expression == 'True':
            return True
        elif expression == 'False':
            return False
        elif expression == 'and':
            return 'and'
        elif expression == 'or':
            return 'or'
        elif expression == 'not':
            return 'not'
        else:
            try:
                return eval(expression, {"__builtins__": None}, context)
            except Exception:
                raise ValueError(f"Invalid expression: {expression}")
    if isinstance(expression, bool):
        return expression
    if isinstance(expression, str):
        if expression == 'True':
            return True
        elif expression == 'False':
            return False
    raise TypeError(f"Unsupported expression type: {type(expression)}")
def safe_evaluate(expression):
    try:
        if isinstance(expression, str):
            if expression == 'True':
                return True
            elif expression == 'False':
                return False
            elif expression == 'and':
                return 'and'
            elif expression == 'or':
                return 'or'
            elif expression == 'not':
                return 'not'
            else:
                return eval(expression, {"__builtins__": None}, {})
        else:
            return expression
    except Exception:
        raise ValueError("Evaluation failed")
if __name__ == '__main__':
    expression1 = "True and not False"
    expression2 = "True"
    try:
        value1 = safe_evaluate(expression1)
        value2 = safe_evaluate(expression2)
        if value1 == value2:
            print("The two expressions evaluate to the same truth value.")
        else:
            print("The two expressions evaluate to different truth values.")
    except ValueError as e:
        print(f"Error during evaluation: {e}")
    except TypeError as e:
        print(f"Type error: {e}")