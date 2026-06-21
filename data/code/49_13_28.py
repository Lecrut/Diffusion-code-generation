class LengthEvaluator:
    @staticmethod
    def _is_within_threshold(length1: int, length2: int, threshold: int) -> bool:
        return abs(length1 - length2) <= threshold

    @classmethod
    def evaluate_lengths(cls, length1: int, length2: int, threshold: int) -> bool:
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative integer.")
        return cls._is_within_threshold(length1, length2, threshold)

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = 5
    result = LengthEvaluator.evaluate_lengths(length1, length2, threshold)
    print(result)