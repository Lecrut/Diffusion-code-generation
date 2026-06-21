import math

def is_valid_triangle(sides):
    return all(a + b > c for a, b, c in [(sides[0], sides[1], sides[2]), 
                                          (sides[0], sides[2], sides[1]), 
                                          (sides[1], sides[2], sides[0])])

def validate_sides(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required to form a triangle.')
    if any(side <= 0 for side in sides):
        raise ValueError('Side lengths must be positive numbers.')
    if not is_valid_triangle(sides):
        raise ValueError('The given sides do not form a valid triangle.')

def calculate_area_with_heron(sides):
    validate_sides(sides)
    a, b, c = sides
    s = sum(sides) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        sides = [5, 6, 7]
        area = calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)