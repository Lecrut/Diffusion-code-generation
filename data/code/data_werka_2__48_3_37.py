import math

def validate_sides(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required to form a triangle.')
    for side in sides:
        if side <= 0:
            raise ValueError('Side lengths must be positive numbers.')
    a, b, c = sides
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')

def calculate_heron_area(sides):
    validate_sides(sides)
    a, b, c = sides
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        sides = [6, 8, 10]
        area = calculate_heron_area(sides)
        print(area)
    except ValueError as e:
        print(e)