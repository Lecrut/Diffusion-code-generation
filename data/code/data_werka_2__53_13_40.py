import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [49, 64, 121]
    for index, area in enumerate(sample_areas):
        side_length = calculate_square_side_length(area)
        print(f"Sample {index + 1}: The side length of the square with area {area} is {side_length}")