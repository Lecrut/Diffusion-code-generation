class NumberEvaluator:
    POSITIVITY_THRESHOLD = 0

    @staticmethod
    def is_positive(value):
        return value > NumberEvaluator.POSITIVITY_THRESHOLD
if __name__ == '__main__':
    print(NumberEvaluator.is_positive(10))
    print(NumberEvaluator.is_positive(-5))
    print(NumberEvaluator.is_positive(0))
    print(NumberEvaluator.is_positive(3.14))
    print(NumberEvaluator.is_positive(-0.001))