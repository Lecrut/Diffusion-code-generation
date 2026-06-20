class OperationEvaluator:

    def evaluate(self, op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b != 0:
                return a / b
            else:
                raise ValueError('Division by zero')
        else:
            raise ValueError('Invalid operation')
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(evaluator.evaluate('+', 5, 3))
    print(evaluator.evaluate('-', 10, 4))
    print(evaluator.evaluate('*', 7, 2))
    try:
        print(evaluator.evaluate('/', 9, 0))
    except ValueError as e:
        print(e)
    try:
        print(evaluator.evaluate('^', 5, 3))
    except ValueError as e:
        print(e)