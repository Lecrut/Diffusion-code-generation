class LogicChecker:
    def evaluate_expression(self, expression):
        try:
            return eval(expression)
        except (SyntaxError, NameError, TypeError) as e:
            raise ValueError(f"Invalid expression: {e}")

if __name__ == '__main__':
    checker = LogicChecker()
    expressions_to_test = [
        "True",
        "False",
        "True and False",
        "not True",
        "5 > 3",
        "10 / 2",
        "3 + '3'",
    ]
    
    for expr in expressions_to_test:
        try:
            result = checker.evaluate_expression(expr)
            print(f"{expr} evaluates to {result}")
        except ValueError as e:
            print(e)