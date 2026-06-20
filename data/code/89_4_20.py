import operator

class MathOperations:

    def __init__(self):
        self.operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow, '%': operator.mod, '//': operator.floordiv}

    def execute(self, num1, num2, operation):
        return self.operations.get(operation, lambda x, y: None)(num1, num2)
if __name__ == '__main__':
    evaluator = MathOperations()
    result_add = evaluator.execute(10, 5, '+')
    result_sub = evaluator.execute(10, 5, '-')
    print(result_add)
    print(result_sub)