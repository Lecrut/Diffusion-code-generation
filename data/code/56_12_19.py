import math

def equilateral_triangle_area(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def isosceles_triangle_area(base, height):
    return 0.5 * base * height

def calculate_ratio(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = equilateral_triangle_area(equilateral_side)
    isosceles_area = isosceles_triangle_area(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        return float('inf')
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    EQUILATERAL_SIDE_LENGTH = 6.0
    ISOSCELES_BASE = 5.0
    ISOSCELES_HEIGHT = 4.0
    ratio = calculate_ratio(EQUILATERAL_SIDE_LENGTH, ISOSCELES_BASE, ISOSCELES_HEIGHT)
    print(ratio)