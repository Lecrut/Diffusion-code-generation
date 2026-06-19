import math

class Triangle:
    @staticmethod
    def equilateral_area(side_length):
        return (math.sqrt(3) / 4) * side_length ** 2

    @staticmethod
    def isosceles_area(base, height):
        return 0.5 * base * height

def calculate_area_ratio(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = Triangle.equilateral_area(equilateral_side)
    isosceles_area = Triangle.isosceles_area(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        return float('inf')
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side_val = 6.0
    isosceles_base_val = 5.0
    isosceles_height_val = 4.0
    ratio = calculate_area_ratio(equilateral_side_val, isosceles_base_val, isosceles_height_val)
    print(ratio)