import math

def equilateral_triangle_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return (math.sqrt(3) / 4) * side_length ** 2

def isosceles_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return 0.5 * base * height

def area_ratio(equilateral_side, isosceles_base, isosceles_height):
    equilateral_area = equilateral_triangle_area(equilateral_side)
    isosceles_area = isosceles_triangle_area(isosceles_base, isosceles_height)
    if isosceles_area == 0:
        raise ZeroDivisionError("Isosceles triangle area cannot be zero for ratio calculation")
    return equilateral_area / isosceles_area

if __name__ == '__main__':
    equilateral_side_val = 6.0
    isosceles_base_val = 8.0
    isosceles_height_val = 4.0
    try:
        ratio = area_ratio(equilateral_side_val, isosceles_base_val, isosceles_height_val)
        print(ratio)
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")