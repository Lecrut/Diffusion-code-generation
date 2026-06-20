import ast

class LogicChecker:
    def is_valid_expression(self, expression):
        try:
            return bool(ast.parse(expression, mode='eval'))
        except SyntaxError:
            raise ValueError("Invalid syntax in the expression")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    checker = LogicChecker()
    test_expressions = [
        "True",
        "False",
        "True and False",
        "not True",
        "5 > 3",
        "True or False",
        "True == True",
        "True == False"
    ]
    
    for expr in test_expressions:
        try:
            result = checker.is_valid_expression(expr)
            print(f"{expr}: {result}")
        except Exception as e:
            print(e)