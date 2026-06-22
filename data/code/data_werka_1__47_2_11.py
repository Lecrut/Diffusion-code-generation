import math
EPSILON = 1e-09

def is_valid_triangle(a, b, c):
    return a + b > c + EPSILON and a + c > b + EPSILON and (b + c > a + EPSILON)

def calculate_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given side lengths do not form a valid triangle.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    side_a = 8.0
    side_b = 15.0
    side_c = 17.0
    try:
        area = calculate_area(side_a, side_b, side_c)
        print(area)
    except ValueError as e:
        print(e)