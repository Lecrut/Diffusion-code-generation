class ConditionEvaluator:
    POSITIVE_THRESHOLD = 0
    REQUIRED_POSITIVE_COUNT = 2

    @staticmethod
    def _is_positive(value: int) -> bool:
        return value > ConditionEvaluator.POSITIVE_THRESHOLD

    @classmethod
    def evaluate_conditions(cls, a: int, b: int, c: int) -> bool:
        positive_count = int(cls._is_positive(a)) + int(cls._is_positive(b)) + int(cls._is_positive(c))
        return positive_count >= cls.REQUIRED_POSITIVE_COUNT

if __name__ == '__main__':
    result = ConditionEvaluator.evaluate_conditions(5, -1, 10)
    print(result)