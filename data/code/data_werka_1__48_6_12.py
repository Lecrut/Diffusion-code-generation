import math

def calculate_triangle_sides(a, b):
    if a <= 0 or b <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    c = math.sqrt(a ** 2 + b ** 2)
    return (a, b, c)
if __name__ == '__main__':
    try:
        side_a = 3
        side_b = 4
        sides = calculate_triangle_sides(side_a, side_b)
        print(sides)
    except ValueError as e:
        print(e)