import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 25.0
    try:
        side_length = calculate_square_side_length(sample_area)
        print(side_length)
    except ValueError as e:
        print(e)