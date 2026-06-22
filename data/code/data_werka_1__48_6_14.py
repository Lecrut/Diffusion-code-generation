import math

def validate_triangle_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("All sides must be positive numbers.")
    if not (c == math.sqrt(a**2 + b**2)):
        raise ValueError("The provided sides do not form a right-angled triangle.")

def calculate_triangle_sides(leg1, leg2):
    validate_triangle_sides(leg1, leg2, math.sqrt(leg1**2 + leg2**2))
    hypotenuse = math.sqrt(leg1**2 + leg2**2)
    return (leg1, leg2, hypotenuse)

if __name__ == '__main__':
    sample_leg1 = 3
    sample_leg2 = 4
    sides = calculate_triangle_sides(sample_leg1, sample_leg2)
    print(sides)