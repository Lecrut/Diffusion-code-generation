import math

class SquareCalculator:
    POWER_EXPONENT = 2

    @staticmethod
    def compute_area(side_length):
        result = math.pow(side_length, SquareCalculator.POWER_EXPONENT)
        return float(result)

if __name__ == '__main__':
    test_value = 7.25
    final_area = SquareCalculator.compute_area(test_value)
    print(final_area)