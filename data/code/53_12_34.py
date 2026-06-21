import math

class Square:
    MIN_AREA = 0.0

    @staticmethod
    def calculate_side_length(area):
        if area < Square.MIN_AREA:
            raise ValueError("Area cannot be negative")
        return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 49.0
    try:
        side_length = Square.calculate_side_length(sample_area)
        print(side_length)
    except ValueError as e:
        print(e)