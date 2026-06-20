class ExpressionEvaluator:
    OPERATIONS = {
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
        '*': lambda num1, num2: num1 * num2,
        '/': lambda num1, num2: num1 / num2 if num2 != 0 else 'Error: Division by zero'
    }

    @staticmethod
    def evaluate_expression(op, num1, num2):
        return ExpressionEvaluator.OPERATIONS.get(op, 'Error: Invalid operator')(num1, num2)

if __name__ == '__main__':
    print(ExpressionEvaluator.evaluate_expression('+', 10, 5))
    print(ExpressionEvaluator.evaluate_expression('-', 20, 8))
    print(ExpressionEvaluator.evaluate_expression('*', 6, 7))