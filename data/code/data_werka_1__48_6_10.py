import math

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    if hypotenuse <= leg1 or hypotenuse <= leg2:
        raise ValueError('Hypotenuse must be the longest side.')
    leg1_squared = leg1 ** 2
    leg2_squared = leg2 ** 2
    hypotenuse_squared = hypotenuse ** 2
    if not math.isclose(leg1_squared + leg2_squared, hypotenuse_squared):
        raise ValueError('The given sides do not form a right-angled triangle.')
    return (leg1, leg2, hypotenuse)
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    hypotenuse = 5
    try:
        sides = calculate_triangle_sides(leg1, leg2, hypotenuse)
        print(sides)
    except ValueError as e:
        print(e)