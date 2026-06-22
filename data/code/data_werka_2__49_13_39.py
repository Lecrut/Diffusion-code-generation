class LengthEvaluator:
    def __init__(self, length1: int, length2: int):
        if not (isinstance(length1, int) and isinstance(length2, int)):
            raise ValueError("Lengths must be integers.")
        self.length1 = length1
        self.length2 = length2

    def evaluate_within_threshold(self, threshold: int) -> bool:
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative integer.")
        return abs(self.length1 - self.length2) <= threshold

if __name__ == '__main__':
    length_evaluator = LengthEvaluator(400, 407)
    threshold = 8
    result = length_evaluator.evaluate_within_threshold(threshold)
    print(result)