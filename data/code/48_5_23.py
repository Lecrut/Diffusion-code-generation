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
        sides = calculate_triangle_sides(3, 4, 5)
        print(sides)
    except ValueError as e:
        print(e)