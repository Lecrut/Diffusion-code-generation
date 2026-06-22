import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    side_length = math.sqrt(area)
    return side_length

if __name__ == '__main__':
    sample_area = 49.0
    try:
        side_length = calculate_square_side_length(sample_area)
        print(f"The side length of the square is: {side_length}")
    except ValueError as e:
        print(e)