import math

def validate_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = {
        'small': 9.0,
        'medium': 16.0,
        'large': 25.0
    }
    for description, area in sample_areas.items():
        try:
            side_length = calculate_square_side_length(area)
            print(f"The side length of the {description} square is: {side_length}")
        except ValueError as e:
            print(e)