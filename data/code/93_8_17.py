class BooleanEvaluator:
    def __init__(self, value1: bool, value2: bool):
        self.value1 = value1
        self.value2 = value2
    
    def are_both_false(self) -> bool:
        return not self.value1 and not self.value2

if __name__ == '__main__':
    evaluator = BooleanEvaluator(False, False)
    print(evaluator.are_both_false())