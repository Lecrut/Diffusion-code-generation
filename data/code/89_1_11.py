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
            raise ValueError(f'Invalid operator: {operator}')

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    print(evaluator.evaluate(10, '+', 5))
    print(evaluator.evaluate(10, '-', 3))
    print(evaluator.evaluate(4, '*', 2))
    try:
        print(evaluator.evaluate(10, '/', 0))
    except ZeroDivisionError as e:
        print(e)
    try:
        print(evaluator.evaluate(10, '%', 5))
    except ValueError as e:
        print(e)