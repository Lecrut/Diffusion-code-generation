import math

def calculate_area_equilateral_triangle(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def calculate_area_isosceles_triangle(base, height):
    return 0.5 * base * height

def calculate_ratio_of_areas(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = calculate_area_equilateral_triangle(equilateral_side)
    isosceles_area = calculate_area_isosceles_triangle(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        return float('inf')
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side_val = 6.0
    isosceles_base_val = 5.0
    isosceles_height_val = 4.0
    ratio = calculate_ratio_of_areas(equilateral_side_val, isosceles_base_val, isosceles_height_val)
    print(ratio)