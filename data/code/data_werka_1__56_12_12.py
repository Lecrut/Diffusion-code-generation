import math

def calculate_equilateral_triangle_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return (math.sqrt(3) / 4) * side_length ** 2

def calculate_isosceles_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return 0.5 * base * height

def calculate_area_ratio(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = calculate_equilateral_triangle_area(equilateral_side)
    isosceles_area = calculate_isosceles_triangle_area(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        raise ValueError("Isosceles triangle area cannot be zero")
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    try:
        equilateral_side = 6.0
        isosceles_base = 8.0
        isosceles_height = 4.0
        ratio = calculate_area_ratio(equilateral_side, isosceles_base, isosceles_height)
        print(ratio)
    except ValueError as e:
        print(f"Error: {e}")