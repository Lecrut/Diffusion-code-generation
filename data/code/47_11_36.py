import math
EPSILON = 1e-09

def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_triangle_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle')
    s = (a + b + c) / 2
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared < EPSILON:
        return 0.0
    return math.sqrt(area_squared)
if __name__ == '__main__':
    try:
        side_a = 6
        side_b = 8
        side_c = 10
        area = calculate_triangle_area(side_a, side_b, side_c)
        print(f'The area of the triangle with sides {side_a}, {side_b}, and {side_c} is: {area}')
    except ValueError as e:
        print(e)