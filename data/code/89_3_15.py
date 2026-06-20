class ExpressionEvaluator:
    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf')
    }

    @staticmethod
    def evaluate(expression):
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("Expression must contain exactly two numbers and one operator.")
        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
        except ValueError:
            raise ValueError("All parts must be valid numbers.")
        if operator not in ExpressionEvaluator.OPERATORS:
            raise ValueError(f"Invalid operator. Must be one of {', '.join(ExpressionEvaluator.OPERATORS.keys())}.")
        return ExpressionEvaluator.OPERATORS[operator](num1, num2)

if __name__ == '__main__':
    result = ExpressionEvaluator.evaluate("5 + 3")
    print(result)