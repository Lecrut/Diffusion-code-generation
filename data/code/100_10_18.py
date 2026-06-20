import ast

class LogicChecker:
    def is_valid_boolean_expression(self, expression):
        try:
            parsed = ast.parse(expression, mode='eval')
            return isinstance(parsed.body, (ast.NameConstant, ast.UnaryOp, ast.BinOp))
        except SyntaxError:
            return False
        except Exception:
            return False

if __name__ == '__main__':
    checker = LogicChecker()
    expressions_to_test = [
        "True",
        "False",
        "True and False",
        "not True",
        "5 > 3"
    ]
    results = [checker.is_valid_boolean_expression(expr) for expr in expressions_to_test]
    print(results)