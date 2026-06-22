import math

def ellipse_area(a, b):
    return math.pi * a * b

def calculate_areas(semi_major_1, semi_minor_1, semi_major_2, semi_minor_2):
    area_1 = ellipse_area(semi_major_1, semi_minor_1)
    area_2 = ellipse_area(semi_major_2, semi_minor_2)
    return area_1, area_2

def area_ratio(area_1, area_2):
    if area_1 > area_2:
        return area_1 / area_2
    else:
        return area_2 / area_1

if __name__ == '__main__':
    semi_major_a = 5
    semi_minor_a = 3
    semi_major_b = 4
    semi_minor_b = 2
    
    areas = calculate_areas(semi_major_a, semi_minor_a, semi_major_b, semi_minor_b)
    ratio = area_ratio(*areas)
    
    print(ratio)