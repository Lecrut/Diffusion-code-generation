import math
EPSILON = 1e-09

def is_right_angled_triangle(leg1, leg2, hypotenuse):
    return math.isclose(leg1 ** 2 + leg2 ** 2, hypotenuse ** 2, rel_tol=EPSILON)

def validate_sides(leg1, leg2, hypotenuse):
    if hypotenuse <= leg1 or hypotenuse <= leg2:
        raise ValueError('Hypotenuse must be the longest side.')
    if not is_right_angled_triangle(leg1, leg2, hypotenuse):
        raise ValueError('The given sides do not form a right-angled triangle.')

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    validate_sides(leg1, leg2, hypotenuse)
    return (leg1, leg2, hypotenuse)
if __name__ == '__main__':
    try:
        leg1 = 6
        leg2 = 8
        hypotenuse = 10
        sides = calculate_triangle_sides(leg1, leg2, hypotenuse)
        print(sides)
    except ValueError as e:
        print(e)