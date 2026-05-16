import ast
def is_valid_boolean_expression(expression):
    try:
        ast.parse(expression, mode='eval')
    except SyntaxError:
        return False
    except ValueError:
        return False
    except Exception:
        return False
    return True
if __name__ == '__main__':
    test_expressions = [
        "True",
        "False",
        "True and False",
        "not True",
        "True or False",
        "True == True",
        "5 > 3",
        "True and",
        "True || False",
        "True == False and",
        "True and True"
    ]
    for expr in test_expressions:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")