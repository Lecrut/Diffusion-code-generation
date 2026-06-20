class BooleanEvaluator:
    @staticmethod
    def evaluate(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    result = BooleanEvaluator.evaluate(True, True)
    print(result)