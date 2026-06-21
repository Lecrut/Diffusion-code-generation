import math

def calculate_triangle_sides(a, b, c):
    if c <= a or c <= b:
        raise ValueError('The hypotenuse must be the longest side.')
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2
    if not math.isclose(a_squared + b_squared, c_squared):
        raise ValueError('The given sides do not form a right-angled triangle.')
    return (a, b, c)
if __name__ == '__main__':
    try:
        side_a = 3
        side_b = 4
        hypotenuse = 5
        sides = calculate_triangle_sides(side_a, side_b, hypotenuse)
        print(sides)
    except ValueError as e:
        print(e)