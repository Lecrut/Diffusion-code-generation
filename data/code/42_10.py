import math

def area_of_ellipse(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    result = area_of_ellipse(10, 5)
    print(result)