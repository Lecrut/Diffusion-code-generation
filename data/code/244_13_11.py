import math

def calculate_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    ellipse1_a = 7
    ellipse1_b = 8
    ellipse2_a = 9
    ellipse2_b = 10
    
    area1 = calculate_ellipse_area(ellipse1_a, ellipse1_b)
    area2 = calculate_ellipse_area(ellipse2_a, ellipse2_b)
    
    total_area = area1 + area2
    print(total_area)