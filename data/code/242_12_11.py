import math
PI = math.pi

def ellipse_area(semi_major, semi_minor):
    return PI * semi_major * semi_minor

def area_ratio():
    SEMI_MAJOR_1, SEMI_MINOR_1 = (5, 3)
    SEMI_MAJOR_2, SEMI_MINOR_2 = (4, 2)
    area_1 = ellipse_area(SEMI_MAJOR_1, SEMI_MINOR_1)
    area_2 = ellipse_area(SEMI_MAJOR_2, SEMI_MINOR_2)
    if area_1 > area_2:
        return area_1 / area_2
    else:
        return area_2 / area_1
if __name__ == '__main__':
    print(area_ratio())