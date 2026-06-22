class LengthChecker:
    def __init__(self, length1: int, length2: int):
        self.length1 = length1
        self.length2 = length2

    def compare_within_threshold(self, threshold: int) -> bool:
        return abs(self.length1 - self.length2) <= threshold

if __name__ == '__main__':
    checker = LengthChecker(length1=400, length2=398)
    print(checker.compare_within_threshold(threshold=7))  # True
    print(checker.compare_within_threshold(threshold=3))  # False