import math

def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_heron_area(a, b, c):
    if not is_valid_triangle(a, b, c):
        raise ValueError('The given sides do not form a valid triangle')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 8
        side_c = 9
        area = calculate_heron_area(side_a, side_b, side_c)
        print(area)
    except ValueError as e:
        print(e)