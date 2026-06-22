import math

def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def calculate_triangle_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given sides do not form a valid triangle')
    return herons_formula(a, b, c)

if __name__ == '__main__':
    side_a = 7
    side_b = 10
    side_c = 5
    try:
        area = calculate_triangle_area(side_a, side_b, side_c)
        print(area)
    except ValueError as e:
        print(e)