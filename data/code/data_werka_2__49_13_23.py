class LengthChecker:
    def __init__(self, length1: int, length2: int):
        self.length1 = length1
        self.length2 = length2

    def _within_tolerance(self, threshold: int) -> bool:
        return abs(self.length1 - self.length2) <= threshold

    def are_lengths_equal_within_threshold(self, threshold: int) -> bool:
        if threshold < 0:
            raise ValueError("Threshold must be a non-negative integer.")
        return self._within_tolerance(threshold)

if __name__ == '__main__':
    length_checker = LengthChecker(300, 295)
    thresholds = [10, 5, 0]
    for threshold in thresholds:
        result = length_checker.are_lengths_equal_within_threshold(threshold)
        print(f"Threshold: {threshold}, Result: {result}")