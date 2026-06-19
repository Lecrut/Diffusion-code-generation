class LengthComparison:
    DEFAULT_THRESHOLD = 10

    @staticmethod
    def compare_lengths(length1: int, length2: int, threshold: int) -> bool:
        return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 395
    threshold = LengthComparison.DEFAULT_THRESHOLD
    result = LengthComparison.compare_lengths(length1, length2, threshold)
    print(result)