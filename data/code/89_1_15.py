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
    result_addition = evaluator.evaluate(7, '+', 3)
    result_subtraction = evaluator.evaluate(12, '-', 4)
    result_multiplication = evaluator.evaluate(5, '*', 6)
    
    print(f"7 + 3 = {result_addition}")
    print(f"12 - 4 = {result_subtraction}")
    print(f"5 * 6 = {result_multiplication}")