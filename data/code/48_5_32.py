import math

def is_hypotenuse_valid(leg1, leg2, hypotenuse):
    return hypotenuse > leg1 and hypotenuse > leg2

def is_right_triangle(leg1, leg2, hypotenuse):
    return math.isclose(leg1**2 + leg2**2, hypotenuse**2)

def validate_sides(leg1, leg2, hypotenuse):
    if not is_hypotenuse_valid(leg1, leg2, hypotenuse):
        raise ValueError('Hypotenuse must be the longest side.')
    if not is_right_triangle(leg1, leg2, hypotenuse):
        raise ValueError('The given sides do not form a right-angled triangle.')

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    validate_sides(leg1, leg2, hypotenuse)
    return (leg1, leg2, hypotenuse)

if __name__ == '__main__':
    try:
        sides = calculate_triangle_sides(6, 8, 10)
        print(sides)
    except ValueError as e:
        print(e)