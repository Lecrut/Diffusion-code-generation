import math

def validate_area(area):
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 49.0
    try:
        side_length = calculate_square_side_length(sample_area)
        print(side_length)
    except ValueError as e:
        print(e)