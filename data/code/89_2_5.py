class ExpressionEvaluator:
    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf')
        }

    def evaluate(self, expression):
        tokens = expression.split()
        if len(tokens) != 3:
            raise ValueError("Invalid input format")
        try:
            num1 = float(tokens[0])
            num2 = float(tokens[2])
        except ValueError:
            raise ValueError("Both operands must be numbers")
        operator = tokens[1]
        if operator not in self.operations:
            raise ValueError("Unsupported operator")
        return self.operations[operator](num1, num2)

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    try:
        result1 = evaluator.evaluate('10 / 2')
        print(result1)
        result2 = evaluator.evaluate('5 * 3')
        print(result2)
        result3 = evaluator.evaluate('8 - 4')
        print(result3)
        result4 = evaluator.evaluate('7 + 6')
        print(result4)
    except ValueError as e:
        print(e)