class BooleanEvaluator:
    def __init__(self, flag1: bool, flag2: bool):
        self.flag1 = flag1
        self.flag2 = flag2

    def are_both_false(self) -> bool:
        return not self.flag1 and not self.flag2

if __name__ == '__main__':
    evaluator = BooleanEvaluator(False, False)
    print(evaluator.are_both_false())