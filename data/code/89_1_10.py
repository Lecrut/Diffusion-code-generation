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
    result_add = evaluator.evaluate(8, '+', 3)
    print(f"8 + 3 = {result_add}")
    result_subtract = evaluator.evaluate(10, '-', 4)
    print(f"10 - 4 = {result_subtract}")
    result_multiply = evaluator.evaluate(5, '*', 6)
    print(f"5 * 6 = {result_multiply}")
    try:
        result_divide = evaluator.evaluate(7, '/', 0)
        print(f"7 / 0 = {result_divide}")
    except ZeroDivisionError as e:
        print(e)