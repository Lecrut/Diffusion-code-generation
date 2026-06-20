class LogicChecker:
    def __init__(self):
        self.valid_operators = {'and', 'or', 'not'}
    
    def is_valid_expression(self, expression):
        try:
            ast.parse(expression, mode='eval')
            return True
        except SyntaxError:
            return False
    
    def evaluate_expression(self, expression):
        if not self.is_valid_expression(expression):
            raise ValueError("Invalid logical expression")
        
        return eval(expression)

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
            print(f"{expr} = {result}")
        except ValueError as e:
            print(e)