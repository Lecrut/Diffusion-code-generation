import math

def ellipse_area(major_axis=10.0, minor_axis=5.0):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    print(ellipse_area())