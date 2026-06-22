import math

def ellipse_area(major_axis=6.0, minor_axis=4.0):
    a = major_axis / 2.0
    b = minor_axis / 2.0
    return math.pi * a * b

if __name__ == '__main__':
    print(ellipse_area())