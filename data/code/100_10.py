import ast
def is_valid_boolean_expression(expression):
    try:
        ast.parse(expression, mode='eval')
        return True
    except SyntaxError:
        return False
    except TypeError:
        return False
    except Exception:
        return False
if __name__ == '__main__':
    expressions_to_test = [
        "True",
        "False",
        "True and False",
        "not True",
        "5 > 3",
        "True or False",
        "True == True and False",
        "True && False"
    ]
    for expr in expressions_to_test:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")