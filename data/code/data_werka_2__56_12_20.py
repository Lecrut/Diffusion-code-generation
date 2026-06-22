import math

def area_of_equilateral_triangle(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def area_of_isosceles_triangle(base, height):
    return 0.5 * base * height

def ratio_of_areas(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = area_of_equilateral_triangle(equilateral_side)
    isosceles_area = area_of_isosceles_triangle(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        raise ValueError("Isosceles triangle height must be greater than zero.")
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side = 6
    isosceles_base = 6
    isosceles_height = 4.5
    ratio = ratio_of_areas(equilateral_side, isosceles_base, isosceles_height)
    print(ratio)