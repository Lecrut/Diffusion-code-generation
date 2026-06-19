import math

def calculate_triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    side_a = 3
    side_b = 4
    side_c = 5
    try:
        area = calculate_triangle_area(side_a, side_b, side_c)
        print(area)
    except ValueError as e:
        print(e)