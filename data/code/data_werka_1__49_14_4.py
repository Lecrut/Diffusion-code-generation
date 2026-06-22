class LengthEvaluator:
    def __init__(self, length1: int, length2: int):
        self.length1 = length1
        self.length2 = length2

    def within_threshold(self, threshold: int) -> bool:
        return abs(self.length1 - self.length2) <= threshold

if __name__ == '__main__':
    evaluator = LengthEvaluator(length1=300, length2=304)
    print(evaluator.within_threshold(threshold=5))  # True
    print(evaluator.within_threshold(threshold=2))  # False