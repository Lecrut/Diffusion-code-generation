class LogicChecker:
    def __init__(self):
        self.valid_operators = {'and', 'or', 'not'}

    def is_valid_boolean_expression(self, expression):
        try:
            eval(expression, {}, {})
            return True
        except (SyntaxError, NameError, TypeError):
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
    for expr in expressions_to_test:
        print(f"Expression: {expr}, Valid: {checker.is_valid_boolean_expression(expr)}")