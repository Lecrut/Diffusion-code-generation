class OperationEvaluator:

    def evaluate(self, a, b, operation):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b != 0:
                return a / b
            else:
                raise ValueError('Cannot divide by zero')
        else:
            raise ValueError('Invalid operation')
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(evaluator.evaluate(10, 5, 'add'))
    print(evaluator.evaluate(10, 5, 'subtract'))
    print(evaluator.evaluate(10, 5, 'multiply'))
    print(evaluator.evaluate(10, 5, 'divide'))