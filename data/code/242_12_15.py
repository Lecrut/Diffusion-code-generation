import math

def ellipse_area(a, b):
    return math.pi * a * b

def area_ratio():
    semi_major_1 = 5
    semi_minor_1 = 3
    semi_major_2 = 4
    semi_minor_2 = 2
    
    area_1 = ellipse_area(semi_major_1, semi_minor_1)
    area_2 = ellipse_area(semi_major_2, semi_minor_2)
    
    if area_1 > area_2:
        larger_area = area_1
        smaller_area = area_2
    else:
        larger_area = area_2
        smaller_area = area_1
    
    return larger_area / smaller_area

if __name__ == '__main__':
    print(area_ratio())