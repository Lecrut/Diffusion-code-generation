import math

def validate_triangle_sides(leg1, leg2, hypotenuse):
    if hypotenuse <= leg1 or hypotenuse <= leg2:
        raise ValueError('Hypotenuse must be the longest side.')
    if not math.isclose(leg1**2 + leg2**2, hypotenuse**2):
        raise ValueError('The given sides do not form a right-angled triangle.')

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    validate_triangle_sides(leg1, leg2, hypotenuse)
    return (leg1, leg2, hypotenuse)

if __name__ == '__main__':
    sample_values = {
        'leg1': 6,
        'leg2': 8,
        'hypotenuse': 10
    }
    
    try:
        sides = calculate_triangle_sides(**sample_values)
        print(sides)
    except ValueError as e:
        print(e)