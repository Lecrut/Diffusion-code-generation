class LengthCalculator:
    DIVISION_ERROR_MESSAGE = "length2 cannot be zero"

    @staticmethod
    def calculate_length_ratio(length1, length2):
        if length2 == 0:
            raise ValueError(LengthCalculator.DIVISION_ERROR_MESSAGE)
        return length1 / length2

if __name__ == '__main__':
    length1 = 7.5
    length2 = 2.5
    ratio = LengthCalculator.calculate_length_ratio(length1, length2)
    print(ratio)