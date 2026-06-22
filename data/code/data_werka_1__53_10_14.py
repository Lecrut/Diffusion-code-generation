import math
SQUARE_AREA = 25.0

def calculate_side_length(area):
    return math.sqrt(area)
if __name__ == '__main__':
    side_length = calculate_side_length(SQUARE_AREA)
    print(f'The side length of the square is: {side_length}')