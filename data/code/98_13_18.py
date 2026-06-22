class ConditionEvaluator:
    MINIMUM_POSITIVE_COUNT = 2

    @staticmethod
    def is_positive(value: int) -> bool:
        return value > 0

    @classmethod
    def evaluate_conditions(cls, a: int, b: int, c: int) -> bool:
        positive_count = sum(
            cls.is_positive(arg)
            for arg in (a, b, c)
        )
        return positive_count >= cls.MINIMUM_POSITIVE_COUNT

if __name__ == '__main__':
    result = ConditionEvaluator.evaluate_conditions(10, -5, 0)
    print(result)