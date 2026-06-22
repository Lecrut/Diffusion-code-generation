class ConditionEvaluator:
    MIN_POSITIVE_THRESHOLD = 2

    @staticmethod
    def _check_positive(value: int) -> bool:
        return value > 0

    @classmethod
    def evaluate_conditions(cls, a: int, b: int, c: int) -> bool:
        positive_count = (
            int(cls._check_positive(a)) +
            int(cls._check_positive(b)) +
            int(cls._check_positive(c))
        )
        return positive_count >= cls.MIN_POSITIVE_THRESHOLD

if __name__ == '__main__':
    result = ConditionEvaluator.evaluate_conditions(1, -2, 3)
    print(result)