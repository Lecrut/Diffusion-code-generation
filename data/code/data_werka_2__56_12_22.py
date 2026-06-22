import math

def area_equilateral_triangle(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def area_isosceles_triangle(base, height):
    return 0.5 * base * height

def ratio_of_areas(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = area_equilateral_triangle(equilateral_side)
    isosceles_area = area_isosceles_triangle(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        raise ValueError("Isosceles triangle height must be greater than zero.")
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side = 5
    isosceles_base = 6
    isosceles_height = 4
    ratio = ratio_of_areas(equilateral_side, isosceles_base, isosceles_height)
    print(ratio)