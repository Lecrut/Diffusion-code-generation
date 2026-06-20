class ExpressionEvaluator:
    def evaluate(self, operand1, operator, operand2):
        if operator == '+':
            return self.add(operand1, operand2)
        elif operator == '-':
            return self.subtract(operand1, operand2)
        elif operator == '*':
            return self.multiply(operand1, operand2)
        elif operator == '/':
            return self.divide(operand1, operand2)
        else:
            raise ValueError(f'Invalid operator: {operator}')

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError('Cannot divide by zero')

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    print(evaluator.evaluate(10, '+', 5))
    print(evaluator.evaluate(10, '-', 3))
    print(evaluator.evaluate(10, '*', 2))
    try:
        print(evaluator.evaluate(10, '/', 0))
    except ZeroDivisionError as e:
        print(e)