import math

def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a

def calculate_area_with_heron(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required to form a triangle.')
    if any(side <= 0 for side in sides):
        raise ValueError('Side lengths must be positive numbers.')
    if not is_valid_triangle(sides):
        raise ValueError('The given sides do not form a valid triangle.')
    
    s = sum(sides) / 2
    area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
    return area

if __name__ == '__main__':
    try:
        sides = [7, 10, 5]
        area = calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)