import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    try:
        sample_area = 16.0
        side_length = calculate_square_side_length(sample_area)
        print(f"The side length of the square is: {side_length}")
    except ValueError as e:
        print(e)