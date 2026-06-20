class LogicEvaluator:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return bool(a or b)

if __name__ == '__main__':
    print(LogicEvaluator.evaluate(True, False))
    print(LogicEvaluator.evaluate(False, True))
    print(LogicEvaluator.evaluate(True, True))
    print(LogicEvaluator.evaluate(False, False))