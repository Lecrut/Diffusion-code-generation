import math

def area_of_ellipse(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    ellipse1_area = area_of_ellipse(3, 2)
    ellipse2_area = area_of_ellipse(4, 1)
    total_area = ellipse1_area + ellipse2_area
    print(total_area)