class BooleanEvaluator:
    def __init__(self, flag1: bool, flag2: bool):
        self.flag1 = flag1
        self.flag2 = flag2

    def evaluate_both_false(self) -> bool:
        return not self.flag1 and not self.flag2

if __name__ == '__main__':
    sample_evaluator = BooleanEvaluator(False, False)
    print(sample_evaluator.evaluate_both_false())