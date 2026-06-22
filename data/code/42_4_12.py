import math

def compute_ellipse_area():
    semi_major_axis = 5
    semi_minor_axis = 3
    area = math.pi * semi_major_axis * semi_minor_axis
    return area

if __name__ == '__main__':
    print(compute_ellipse_area())