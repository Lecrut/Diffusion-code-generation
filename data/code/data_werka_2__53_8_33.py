import math
SQUARE_AREA = 25.0

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError('Area cannot be negative')
    return math.sqrt(area)
if __name__ == '__main__':
    try:
        side_length = calculate_square_side_length(SQUARE_AREA)
        print(f'The side length of the square is: {side_length}')
    except ValueError as e:
        print(e)