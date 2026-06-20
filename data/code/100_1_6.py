class LogicEvaluator:
    @staticmethod
    def check_logic(A: bool, B: bool, C: bool) -> bool:
        return A and (B or not C)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.check_logic(True, False, True))