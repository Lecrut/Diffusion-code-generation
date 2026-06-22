class LengthEvaluator:
    DEFAULT_THRESHOLD = 5

    @staticmethod
    def _compare_lengths(length1: int, length2: int, threshold: int) -> bool:
        return abs(length1 - length2) <= threshold

    def are_equal_within_threshold(self, length1: int, length2: int, threshold: int = DEFAULT_THRESHOLD) -> bool:
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative integer.")
        return LengthEvaluator._compare_lengths(length1, length2, threshold)

if __name__ == '__main__':
    length_evaluator = LengthEvaluator()
    length1 = 400
    length2 = 407
    threshold = 8
    result = length_evaluator.are_equal_within_threshold(length1, length2, threshold)
    print(result)