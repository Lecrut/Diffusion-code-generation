import ast
def is_valid_boolean_expression(expression):
    try:
        ast.parse(expression, mode='eval')
        return True
    except SyntaxError:
        return False
    except TypeError:
        return False
if __name__ == '__main__':
    expressions_to_test = [
        "True",
        "False",
        "True and False",
        "not True",
        "True or False",
        "True == True",
        "True == False",
        "True == 'True'",
        "True and",
        "True or",
        "True ==",
        "True and True",
        "True or False and True"
    ]
    for expr in expressions_to_test:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")