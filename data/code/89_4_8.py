import operator

class MathEvaluator:
    def __init__(self):
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            '%': operator.mod,
            '//': operator.floordiv
        }

    def evaluate(self, num1, num2, operation):
        return self.ops[operation](num1, num2)

if __name__ == '__main__':
    evaluator = MathEvaluator()
    result_add = evaluator.evaluate(10, 5, '+')
    result_sub = evaluator.evaluate(10, 5, '-')
    print(result_add)
    print(result_sub)