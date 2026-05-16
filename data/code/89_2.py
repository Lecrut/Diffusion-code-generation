class InvalidOperationError(Exception):
    pass
class ExpressionEvaluator:
    def evaluate(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise InvalidOperationError("Division by zero is not allowed")
            return operand1 / operand2
        else:
            raise InvalidOperationError(f"Invalid operator: {operator}")
if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    try:
        result1 = evaluator.evaluate(10, 5, '+')
        print(f"10 + 5 = {result1}")
        result2 = evaluator.evaluate(20, 4, '*')
        print(f"20 * 4 = {result2}")
        result3 = evaluator.evaluate(100, 0, '/')
        print(f"100 / 0 = {result3}")
        result4 = evaluator.evaluate(10, 3, '%')
        print(f"10 % 3 = {result4}")
    except InvalidOperationError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")