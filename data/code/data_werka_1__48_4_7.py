import math

def calculate_area_with_heron(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three side lengths are required for a triangle.')
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid side lengths: do not satisfy the triangle inequality.')
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        sides = [5, 12, 13]
        area = calculate_area_with_heron(sides)
        print(f"The area of the triangle with sides {sides} is: {area}")
    except ValueError as e:
        print(e)