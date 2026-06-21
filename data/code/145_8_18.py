class PredicateEvaluator:

    def __init__(self, values):
        self.values = values

    def evaluate(self, predicate):
        return predicate(self.values)
if __name__ == '__main__':
    evaluator = PredicateEvaluator([1, 2, 3, 4, 5])
    print(evaluator.evaluate(lambda x: all((i % 2 != 0 for i in x))))
    print(evaluator.evaluate(lambda x: any((i % 2 == 0 for i in x))))