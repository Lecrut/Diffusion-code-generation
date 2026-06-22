import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 49.0
    try:
        side_length = calculate_square_side_length(sample_area)
        print(f"The side length of the square with area {sample_area} is: {side_length}")
    except ValueError as e:
        print(e)