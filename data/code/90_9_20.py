class ConditionEvaluator:
    def check_condition(self, *args):
        return any(args)

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(evaluator.check_condition(True, False, False))
    print(evaluator.check_condition(False, False, True))
    print(evaluator.check_condition(False, False, False))