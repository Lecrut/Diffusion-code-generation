class LogicalEvaluator:
    @staticmethod
    def evaluate_statements():
        yield True and False
        yield 1 == 2
        yield not (3 > 4)
        yield 'a' in 'abc'
        yield len([1, 2, 3]) == 3

if __name__ == '__main__':
    evaluator = LogicalEvaluator()
    for result in evaluator.evaluate_statements():
        print(result)