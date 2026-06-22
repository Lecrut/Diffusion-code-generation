import math

def validate_side_length(side):
    if side <= 0:
        raise ValueError("Side length must be positive")

def equilateral_triangle_area(side):
    validate_side_length(side)
    return (math.sqrt(3) / 4) * side ** 2

def isosceles_triangle_area(base, height):
    validate_side_length(base)
    validate_side_length(height)
    return (1/2) * base * height

def area_ratio(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = equilateral_triangle_area(equilateral_side)
    isosceles_area = isosceles_triangle_area(isosceles_base, isosceles_height)
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side_val = 6.0
    isosceles_base_val = 8.0
    isosceles_height_val = 5.0
    ratio = area_ratio(equilateral_side_val, isosceles_base_val, isosceles_height_val)
    print(ratio)