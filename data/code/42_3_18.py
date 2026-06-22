import math

def area_of_ellipse(major_axis, minor_axis):
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    result = area_of_ellipse(10, 6)
    print(result)