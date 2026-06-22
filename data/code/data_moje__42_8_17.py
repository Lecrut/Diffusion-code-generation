import math

def get_ellipse_area():
    major_axis = 10
    minor_axis = 6
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    area = get_ellipse_area()
    print(area)