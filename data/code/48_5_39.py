import math

def calculate_triangle_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("Side lengths must be positive")
    
    sides = sorted([a, b, c])
    a, b, hypotenuse = sides
    
    if not math.isclose(hypotenuse**2, a**2 + b**2):
        raise ValueError("The given sides do not form a right-angled triangle")
    
    return a, b, hypotenuse

if __name__ == '__main__':
    try:
        side_a = 3
        side_b = 4
        hypotenuse = 5
        result = calculate_triangle_sides(side_a, side_b, hypotenuse)
        print(result)
    except ValueError as e:
        print(e)