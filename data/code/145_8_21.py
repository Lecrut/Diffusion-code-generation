class PredicateEvaluator:
    def __init__(self, predicates):
        self.predicates = predicates

    def evaluate(self):
        for predicate in self.predicates:
            if not predicate():
                return False
        return True

if __name__ == '__main__':
    sample_values = [
        lambda: 1 > 0,
        lambda: 2 < 3,
        lambda: 4 == 4
    ]
    evaluator = PredicateEvaluator(sample_values)
    print(evaluator.evaluate())