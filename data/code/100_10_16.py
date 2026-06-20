import ast

class LogicChecker:
    def evaluate_expression(self, expression):
        try:
            return eval(expression)
        except SyntaxError:
            raise ValueError("Invalid syntax in expression")
        except NameError:
            raise ValueError("Undefined names in expression")

if __name__ == '__main__':
    checker = LogicChecker()
    expressions_to_test = [
        "True",
        "False",
        "True and False",
        "not True",
        "5 > 3"
    ]
    for expr in expressions_to_test:
        try:
            result = checker.evaluate_expression(expr)
            print(f"{expr} evaluates to {result}")
        except ValueError as e:
            print(e)