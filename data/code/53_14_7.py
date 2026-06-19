import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    hard_coded_area = 20.25
    try:
        side_length_result = calculate_square_side_length(hard_coded_area)
        print(f"The side length of the square is: {side_length_result}")
    except ValueError as e:
        print(e)