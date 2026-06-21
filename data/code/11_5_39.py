class RatioCalculator:
    MIN_LENGTH = 1

    @staticmethod
    def validate_length(length):
        if length <= 0:
            raise ValueError("Both lengths must be positive")

    @classmethod
    def calculate_ratio(cls, length1, length2):
        cls.validate_length(length1)
        cls.validate_length(length2)
        return length1 / length2

if __name__ == '__main__':
    length1 = 8
    length2 = 4
    ratio = RatioCalculator.calculate_ratio(length1, length2)
    print(ratio)