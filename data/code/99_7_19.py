import ast

def evaluate_boolean_expression(expression):
    if not expression:
        return None
    
    try:
        tree = ast.parse(expression, mode='eval')
        compiled_code = compile(tree, filename="<ast>", mode="eval")
        result = eval(compiled_code)
        return result
    except (SyntaxError, NameError) as e:
        return f"Error: {e}"

if __name__ == '__main__':
    print(evaluate_boolean_expression("3 > 2 and not False"))
    print(evaluate_boolean_expression("(True or False) and True"))
    print(evaluate_boolean_expression("not(1 == 2)"))