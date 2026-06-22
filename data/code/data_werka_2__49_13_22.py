class LengthComparator:
    def __init__(self, length1: int, length2: int):
        self.length1 = length1
        self.length2 = length2

    def are_equal_within_threshold(self, threshold: int) -> bool:
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative integer.")
        return abs(self.length1 - self.length2) <= threshold

if __name__ == '__main__':
    length_comparator = LengthComparator(200, 203)
    threshold = 4
    result = length_comparator.are_equal_within_threshold(threshold)
    print(result)