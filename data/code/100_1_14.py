class LogicEvaluator:
    @staticmethod
    def check_logic(A, B, C):
        return A and (B or not C)

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.check_logic(True, False, True))
    print(evaluator.check_logic(False, True, False))