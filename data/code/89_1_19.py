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
                raise ValueError('Division by zero')
        else:
            raise ValueError(f'Invalid operator: {operator}')

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    result_addition = evaluator.evaluate(8, '+', 3)
    print(f"8 + 3 = {result_addition}")
    
    result_subtraction = evaluator.evaluate(15, '-', 7)
    print(f"15 - 7 = {result_subtraction}")
    
    result_multiplication = evaluator.evaluate(4, '*', 6)
    print(f"4 * 6 = {result_multiplication}")
    
    try:
        result_division = evaluator.evaluate(10, '/', 0)
        print(result_division)
    except ValueError as e:
        print(e)
    
    try:
        result_invalid_operator = evaluator.evaluate(5, '^', 2)
        print(result_invalid_operator)
    except ValueError as e:
        print(e)