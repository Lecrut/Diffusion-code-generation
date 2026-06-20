class InvalidOperationError(Exception):
    def __init__(self, message):
        self.message = message

class ExpressionEvaluator:
    def evaluate(self, operand1, operator, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 != 0:
                return operand1 / operand2
            else:
                raise ZeroDivisionError('Cannot divide by zero')
        else:
            raise InvalidOperationError(f'Invalid operator: {operator}')

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    print(evaluator.evaluate(10, '+', 5))
    try:
        print(evaluator.evaluate(10, '/', 0))
    except ZeroDivisionError as e:
        print(e)
    try:
        print(evaluator.evaluate(10, '%', 5))
    except InvalidOperationError as e:
        print(e)