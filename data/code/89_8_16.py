class OperationEvaluator:
    operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else 'Error: Division by zero'}

    def evaluate(self, a, b, op):
        if op in self.operations:
            return self.operations[op](a, b)
        else:
            raise ValueError(f'Unsupported operation: {op}')
if __name__ == '__main__':
    evaluator = OperationEvaluator()
    print(evaluator.evaluate(10, 5, '+'))
    print(evaluator.evaluate(10, 5, '-'))
    print(evaluator.evaluate(10, 5, '*'))
    print(evaluator.evaluate(10, 5, '/'))
    try:
        print(evaluator.evaluate(10, 0, '/'))
    except ValueError as e:
        print(e)