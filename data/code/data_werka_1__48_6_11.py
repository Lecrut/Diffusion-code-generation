import math

def calculate_triangle_sides(a, b, c):
    if a > c or b > c:
        raise ValueError('The hypotenuse must be the longest side.')
    if not math.isclose(a ** 2 + b ** 2, c ** 2):
        raise ValueError('The given sides do not form a right-angled triangle.')
    return (a, b, c)
if __name__ == '__main__':
    leg1 = 3
    leg2 = 4
    hypotenuse = 5
    try:
        sides = calculate_triangle_sides(leg1, leg2, hypotenuse)
        print(sides)
    except ValueError as e:
        print(e)