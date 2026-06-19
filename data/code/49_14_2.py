class LengthComparator:
    def __init__(self, length1: int, length2: int, threshold: int):
        self.length1 = length1
        self.length2 = length2
        self.threshold = threshold

    def are_equal_within_threshold(self) -> bool:
        return abs(self.length1 - self.length2) <= self.threshold

if __name__ == '__main__':
    comparator = LengthComparator(length1=150, length2=148, threshold=3)
    result = comparator.are_equal_within_threshold()
    print(result)