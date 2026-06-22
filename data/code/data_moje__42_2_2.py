import math

def calculate_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    result = calculate_ellipse_area(5, 3)
    print(result)