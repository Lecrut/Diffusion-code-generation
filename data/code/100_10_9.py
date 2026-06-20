class LogicChecker:
    def evaluate_expression(self, expression):
        allowed_operators = {'and', 'or', 'not'}
        if not all(char.isalnum() or char in allowed_operators for char in expression):
            return False

        try:
            result = eval(expression)
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
        "5 > 3",
        "a == b",
        "1 + 2"
    ]
    
    for expr in expressions_to_test:
        print(f"Expression: {expr}, Valid: {checker.evaluate_expression(expr)}")