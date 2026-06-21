class DimensionCalculator:
    MIN_LENGTH = 0

    @staticmethod
    def calculate_ratio(length1, length2):
        if length1 <= DimensionCalculator.MIN_LENGTH or length2 <= DimensionCalculator.MIN_LENGTH:
            raise ValueError("Both lengths must be positive")
        return length1 / length2

if __name__ == '__main__':
    try:
        length1 = 8
        length2 = 4
        ratio = DimensionCalculator.calculate_ratio(length1, length2)
        print(ratio)
    except ValueError as e:
        print(e)