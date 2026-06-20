class ExpressionEvaluator:
    SUPPORTED_OPERATORS = {'+', '-', '*', '/'}

    @staticmethod
    def is_valid_operator(operator):
        return operator in ExpressionEvaluator.SUPPORTED_OPERATORS

    def evaluate(self, operand1, operator, operand2):
        if not self.is_valid_operator(operator):
            raise ValueError(f"Invalid operation: {operator}")
        
        if operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
        
        return eval(f"{operand1}{operator}{operand2}")

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