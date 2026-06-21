import math
MIN_SIDE_LENGTH = 1e-06

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and (b + c > a)

def calculate_triangle_area(a, b, c):
    if not all((side > MIN_SIDE_LENGTH for side in (a, b, c))):
        raise ValueError('Side lengths must be positive')
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        side_a = 3.0
        side_b = 4.0
        side_c = 5.0
        area = calculate_triangle_area(side_a, side_b, side_c)
        print(f'The area of the triangle with sides {side_a}, {side_b}, and {side_c} is: {area}')
    except ValueError as e:
        print(e)