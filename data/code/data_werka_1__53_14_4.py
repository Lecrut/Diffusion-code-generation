import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [9.0, 16.0, 25.0, -4.0]
    for index, area in enumerate(sample_areas):
        try:
            side_length = calculate_square_side_length(area)
            print(f"Sample {index + 1}: The side length of the square with area {area} is {side_length}")
        except ValueError as e:
            print(f"Sample {index + 1}: Error - {e}")