import math

def calculate_triangle_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("Side lengths must be positive numbers.")
    
    sides = sorted([a, b, c])
    a, b, hypotenuse = sides[0], sides[1], sides[2]
    
    if not math.isclose(hypotenuse**2, a**2 + b**2):
        raise ValueError("The given sides do not form a right-angled triangle.")
    
    return a, b, hypotenuse

if __name__ == '__main__':
    try:
        side_a = 3
        side_b = 4
        side_c = 5
        sides = calculate_triangle_sides(side_a, side_b, side_c)
        print(sides)
    except ValueError as e:
        print(e)