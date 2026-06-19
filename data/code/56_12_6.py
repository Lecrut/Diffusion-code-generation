import math

def area_equilateral_triangle(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def area_isosceles_triangle(base, height):
    return 0.5 * base * height

def ratio_of_areas(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = area_equilateral_triangle(equilateral_side)
    isosceles_area = area_isosceles_triangle(isosceles_base, isosceles_height)
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side_length = 6
    isosceles_base_length = 8
    isosceles_height_length = 5
    ratio = ratio_of_areas(equilateral_side_length, isosceles_base_length, isosceles_height_length)
    print(ratio)