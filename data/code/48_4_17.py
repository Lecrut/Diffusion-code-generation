import math

def calculate_heron_area(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required for a triangle.')
    
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Side lengths must be positive numbers.')
    
    semi_perimeter = (a + b + c) / 2
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given sides do not form a valid triangle.')
    
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return area

if __name__ == '__main__':
    try:
        side_lengths = [5, 12, 13]
        triangle_area = calculate_heron_area(side_lengths)
        print(f"The area of the triangle with sides {side_lengths} is: {triangle_area}")
    except ValueError as e:
        print(e)