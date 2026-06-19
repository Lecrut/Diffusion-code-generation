import math
MIN_VALID_SIDE_LENGTH = 0.1
MAX_VALID_SIDES = 3

def calculate_area_with_heron(sides):
    if len(sides) != MAX_VALID_SIDES:
        raise ValueError('Exactly three sides are required for a triangle.')
    for side in sides:
        if side <= MIN_VALID_SIDE_LENGTH:
            raise ValueError('Side lengths must be greater than zero.')
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        area = calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)