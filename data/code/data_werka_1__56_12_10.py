import math

def equilateral_triangle_area(side_length):
    return (math.sqrt(3) / 4) * side_length ** 2

def isosceles_triangle_area(base, height):
    return 0.5 * base * height

def area_ratio(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = equilateral_triangle_area(equilateral_side)
    isosceles_area = isosceles_triangle_area(isosceles_base, isosceles_height)
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side_length = 6
    isosceles_base_length = 8
    isosceles_height_length = 5
    ratio = area_ratio(equilateral_side_length, isosceles_base_length, isosceles_height_length)
    print(ratio)