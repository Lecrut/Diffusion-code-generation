import math

def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a

def calculate_heron_area(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required to form a triangle.')
    if any(side <= 0 for side in sides):
        raise ValueError('Side lengths must be positive numbers.')
    if not is_valid_triangle(sides):
        raise ValueError('The given sides do not form a valid triangle.')
    
    semi_perimeter = sum(sides) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - sides[0]) * (semi_perimeter - sides[1]) * (semi_perimeter - sides[2]))
    return area

if __name__ == '__main__':
    try:
        sides = [6, 8, 10]
        area = calculate_heron_area(sides)
        print(area)
    except ValueError as e:
        print(e)