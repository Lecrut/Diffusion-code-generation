import math

class SquareCalculator:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    try:
        sample_square = SquareCalculator(25.0)
        side_length = sample_square.calculate_side_length()
        print(f"The side length of the square is: {side_length}")
    except ValueError as e:
        print(e)