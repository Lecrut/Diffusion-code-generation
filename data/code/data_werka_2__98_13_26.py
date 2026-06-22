class ConditionEvaluator:
    MIN_POSITIVE_THRESHOLD = 2

    @staticmethod
    def evaluate_conditions(a: int, b: int, c: int) -> bool:
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
            raise ValueError("All arguments must be integers")
        positive_count = (a > 0) + (b > 0) + (c > 0)
        return positive_count >= ConditionEvaluator.MIN_POSITIVE_THRESHOLD

if __name__ == '__main__':
    result = ConditionEvaluator.evaluate_conditions(1, -2, 3)
    print(result)
    result2 = ConditionEvaluator.evaluate_conditions(-1, -2, -3)
    print(result2)
    result3 = ConditionEvaluator.evaluate_conditions(0, 5, 5)
    print(result3)