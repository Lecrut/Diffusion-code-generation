class BooleanEvaluator:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        c = a or not b
        return (a and b) or (not a and c)

if __name__ == '__main__':
    print(BooleanEvaluator.evaluate(True, False))
    print(BooleanEvaluator.evaluate(False, True))
    print(BooleanEvaluator.evaluate(True, True))
    print(BooleanEvaluator.evaluate(False, False))