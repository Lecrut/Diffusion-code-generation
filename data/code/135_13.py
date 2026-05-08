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
            node = ast.parse(expression, mode='eval')
            return eval(compile(node, '<string>', 'eval'), context)
        except Exception:
            return None
def safe_evaluate(expression):
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
            try:
                node = ast.parse(expression, mode='eval')
                return eval(compile(node, '<string>', 'eval'))
            except Exception:
                return None
    return None
if __name__ == '__main__':
    expression1 = "True and not False"
    expression2 = "True"
    value1 = safe_evaluate(expression1)
    value2 = safe_evaluate(expression2)
    if value1 is not None and value2 is not None:
        if value1 == value2:
            print("The two expressions evaluate to the same truth value.")
        else:
            print("The two expressions evaluate to different truth values.")
    else:
        print("Error during evaluation of one or both expressions.")