class ConditionEvaluator:
    @staticmethod
    def evaluate_or(pair):
        return pair[0] or pair[1]

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(evaluator.evaluate_or((True, False)))
    print(evaluator.evaluate_or((False, True)))
    print(evaluator.evaluate_or((False, False)))
    print(evaluator.evaluate_or((None, True)))
    print(evaluator.evaluate_or((0, True)))