import math

def calculate_hypotenuse(leg1, leg2):
    return math.sqrt(leg1**2 + leg2**2)

def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def validate_sides(leg1, leg2, hypotenuse):
    if hypotenuse <= leg1 or hypotenuse <= leg2:
        raise ValueError('Hypotenuse must be the longest side.')
    if not is_right_triangle(leg1, leg2, hypotenuse):
        raise ValueError('The given sides do not form a right-angled triangle.')

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    validate_sides(leg1, leg2, hypotenuse)
    return (leg1, leg2, hypotenuse)

if __name__ == '__main__':
    leg1 = 6
    leg2 = 8
    hypotenuse = 10
    try:
        sides = calculate_triangle_sides(leg1, leg2, hypotenuse)
        print(sides)
    except ValueError as e:
        print(e)