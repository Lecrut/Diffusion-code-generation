class LengthRatioCalculator:
    DEFAULT_PRECISION = 10

    @staticmethod
    def calculate_ratio(length1, length2):
        if length2 == 0:
            raise ValueError("Length2 cannot be zero.")
        return length1 / length2

    @classmethod
    def print_ratio(cls, length1, length2):
        try:
            ratio = cls.calculate_ratio(length1, length2)
            print(f"The ratio of {length1} to {length2} is: {ratio:.{cls.DEFAULT_PRECISION}f}")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    LengthRatioCalculator.print_ratio(15.75, 3.25)