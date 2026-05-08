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
    test_expressions = [
        "True",
        "False",
        "True and False",
        "not True",
        "5 > 3",
        "True or False",
        "True == True",
        "True and",
        "True or",
        "True ==",
        "True and True"
    ]
    for expr in test_expressions:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")