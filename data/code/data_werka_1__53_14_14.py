import math

def validate_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [25.0, 36.0, 49.0]
    for index, area in enumerate(sample_areas):
        try:
            side_length = calculate_square_side_length(area)
            print(f"Sample {index + 1}: The side length of the square with area {area} is {side_length}")
        except ValueError as e:
            print(e)