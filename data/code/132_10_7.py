class LogicEvaluator:
    @staticmethod
    def evaluate(a: bool, b: bool, c: bool) -> bool:
        return (a and b) or not c

if __name__ == '__main__':
    print(LogicEvaluator.evaluate(True, False, True))
    print(LogicEvaluator.evaluate(False, False, False))
    print(LogicEvaluator.evaluate(True, True, False))
    print(LogicEvaluator.evaluate(False, True, True))