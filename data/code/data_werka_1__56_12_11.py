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
    triangle_sides = {
        'equilateral': 6.0,
        'isosceles_base': 8.0,
        'isosceles_height': 4.0
    }
    
    ratio = area_ratio(triangle_sides['equilateral'], triangle_sides['isosceles_base'], triangle_sides['isosceles_height'])
    print(ratio)