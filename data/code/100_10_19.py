import ast

class LogicChecker:

    @staticmethod
    def is_valid_boolean_expression(expression):
        try:
            ast.parse(expression, mode='eval')
            return True
        except SyntaxError:
            return False

    def evaluate_expression(self, expression):
        if not self.is_valid_boolean_expression(expression):
            raise ValueError('Invalid boolean expression')
        return eval(expression)
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate_expression('True and False'))
    print(checker.evaluate_expression('not True'))