import math

def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [16, 25, 81, 0, 49]
    for area in sample_areas:
        try:
            side_length = calculate_square_side_length(area)
            print(f"The side length of a square with area {area} is: {side_length}")
        except (TypeError, ValueError) as e:
            print(e)