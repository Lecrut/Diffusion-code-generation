import operator

class MathEvaluator:
    OPS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }

    @staticmethod
    def evaluate(num1, num2, operation):
        return MathEvaluator.OPS.get(operation, lambda x, y: None)(num1, num2)

if __name__ == '__main__':
    evaluator = MathEvaluator()
    result_add = evaluator.evaluate(10, 5, '+')
    result_sub = evaluator.evaluate(10, 5, '-')
    print(result_add)
    print(result_sub)