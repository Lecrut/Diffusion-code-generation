import math

def hexagon_area(side_length):
    return 3 * math.sqrt(3) / 2 * side_length ** 2

def validate_side_length(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be a positive number')
if __name__ == '__main__':
    try:
        validate_side_length(2)
        area_2 = hexagon_area(2)
        validate_side_length(3)
        area_3 = hexagon_area(3)
        total_area = area_2 + area_3
        print(total_area)
    except ValueError as e:
        print(e)