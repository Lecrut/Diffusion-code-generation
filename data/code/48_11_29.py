import math
SQUARE_AREA = 16

def calculate_square_properties(area):
    side_length = math.sqrt(area)
    perimeter = 4 * side_length
    return (side_length, perimeter)
if __name__ == '__main__':
    try:
        side_length, perimeter = calculate_square_properties(SQUARE_AREA)
        print(f'Side Length: {side_length}, Perimeter: {perimeter}')
    except ValueError as e:
        print(e)