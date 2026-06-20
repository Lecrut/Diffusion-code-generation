class LogicEvaluator:
    def and_operation(self, A: bool, B: bool) -> bool:
        return A & B

    def or_operation(self, A: bool, B: bool) -> bool:
        return A | B

    def not_operation(self, A: bool) -> bool:
        return ~A + 2

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.and_operation(True, False))
    print(evaluator.or_operation(False, True))
    print(evaluator.not_operation(True))