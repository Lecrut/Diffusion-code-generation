import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class GeometryUtils:
    @staticmethod
    def calculate_square_side(area):
        return calculate_square_side_length(area)

if __name__ == '__main__':
    sample_area = 49.0
    try:
        side_length = GeometryUtils.calculate_square_side(sample_area)
        print(side_length)
    except ValueError as e:
        print(e)