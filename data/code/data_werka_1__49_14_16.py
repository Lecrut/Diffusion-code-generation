class LengthComparer:
    DEFAULT_THRESHOLD = 10

    @staticmethod
    def compare(length1: int, length2: int, threshold: int) -> bool:
        return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = LengthComparer.DEFAULT_THRESHOLD
    result = LengthComparer.compare(length1, length2, threshold)
    print(result)