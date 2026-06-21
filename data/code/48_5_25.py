import math

def calculate_triangle_sides(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("Side lengths must be positive")
    
    sides = sorted([a, b, c])
    
    if not math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2):
        raise ValueError("The given sides do not form a right-angled triangle")
    
    return sides

if __name__ == '__main__':
    try:
        result = calculate_triangle_sides(3, 4, 5)
        print(result)
    except ValueError as e:
        print(e)