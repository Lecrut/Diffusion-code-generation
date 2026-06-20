class OperationEvaluator:

    def evaluate(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b != 0:
                return a / b
            else:
                raise ValueError('Division by zero')
        else:
            raise ValueError('Invalid operation')
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(evaluator.evaluate(10, 5, '+'))
    print(evaluator.evaluate(10, 5, '-'))
    print(evaluator.evaluate(10, 5, '*'))
    try:
        print(evaluator.evaluate(10, 0, '/'))
    except ValueError as e:
        print(e)
    try:
        print(evaluator.evaluate(10, 5, '^'))
    except ValueError as e:
        print(e)