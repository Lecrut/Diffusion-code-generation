import math

class SquareCalculator:
    @staticmethod
    def find_side_length(area):
        return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 25.0
    side_length = SquareCalculator.find_side_length(sample_area)
    print(side_length)