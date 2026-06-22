import math

def calculate_triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
if __name__ == '__main__':
    try:
        side1 = 3
        side2 = 4
        side3 = 5
        area = calculate_triangle_area(side1, side2, side3)
        print(area)
    except ValueError as e:
        print(e)