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
        result_add = evaluator.evaluate('5 + 3')
        result_sub = evaluator.evaluate('10 - 4')
        result_mul = evaluator.evaluate('7 * 6')
        result_div = evaluator.evaluate('8 / 2')
        
        print("Addition Result:", result_add)
        print("Subtraction Result:", result_sub)
        print("Multiplication Result:", result_mul)
        print("Division Result:", result_div)
    except ValueError as e:
        print(e)