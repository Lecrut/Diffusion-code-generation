import math

def calculate_triangle_sides(leg1, leg2, hypotenuse):
    if hypotenuse <= 0 or leg1 <= 0 or leg2 <= 0:
        raise ValueError("All sides must be positive numbers.")
    
    if not (math.isclose(hypotenuse**2, leg1**2 + leg2**2)):
        raise ValueError("The given sides do not form a right-angled triangle.")
    
    return leg1, leg2, hypotenuse

if __name__ == '__main__':
    try:
        side_lengths = calculate_triangle_sides(3, 4, 5)
        print(side_lengths)
    except ValueError as e:
        print(e)