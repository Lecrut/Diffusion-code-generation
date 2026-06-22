import math

def ellipse_area(major_axis=2.0, minor_axis=1.0):
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    print(ellipse_area())