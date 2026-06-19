import math

def calculate_area_with_heron(sides):
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required for a triangle.")
    
    a, b, c = sides
    
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == '__main__':
    try:
        sides = [5, 12, 13]
        area = calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)