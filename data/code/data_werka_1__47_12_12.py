import math
MIN_SIDE_LENGTH = 1e-09

def calculate_triangle_area(a, b, c):
    if a < MIN_SIDE_LENGTH or b < MIN_SIDE_LENGTH or c < MIN_SIDE_LENGTH:
        raise ValueError('Side lengths must be positive')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        side1 = 7.0
        side2 = 8.0
        side3 = 9.0
        area = calculate_triangle_area(side1, side2, side3)
        print(area)
    except ValueError as e:
        print(e)