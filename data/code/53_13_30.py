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
    sample_areas = {
        'square1': 36,
        'square2': 49,
        'square3': 64
    }
    for name, area in sample_areas.items():
        try:
            side_length = calculate_square_side_length(area)
            print(f"The side length of {name} is: {side_length}")
        except (TypeError, ValueError) as e:
            print(f"Error calculating side length for {name}: {e}")