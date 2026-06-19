import math

def validate_triangle_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("Side lengths must be positive")
    if not (c == max(a, b, c)):
        raise ValueError("The hypotenuse must be the longest side")

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    validate_triangle_sides(leg1, leg2, hypotenuse)
    return leg1, leg2, hypotenuse

if __name__ == '__main__':
    sample_leg1 = 3
    sample_leg2 = 4
    sample_hypotenuse = 5
    sides = calculate_triangle_sides(sample_leg1, sample_leg2, sample_hypotenuse)
    print(sides)