import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calculate_heron_area(sides):
    if len(sides) != 3:
        raise ValueError("Exactly three side lengths are required for a triangle.")
    a, b, c = sides
    if not all(side > 0 for side in sides):
        raise ValueError("Side lengths must be positive numbers.")
    if not is_valid_triangle(a, b, c):
        raise ValueError("The given sides do not form a valid triangle.")
    
    semi_perimeter = (a + b + c) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return area

if __name__ == '__main__':
    try:
        side_lengths = [5, 12, 13]
        triangle_area = calculate_heron_area(side_lengths)
        print(f"The area of the triangle is: {triangle_area}")
    except ValueError as e:
        print(e)