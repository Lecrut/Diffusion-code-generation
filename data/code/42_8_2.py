import math

def ellipse_area(major_axis=6.0, minor_axis=4.0):
    return math.pi * major_axis * minor_axis / 4.0

if __name__ == '__main__':
    print(ellipse_area())