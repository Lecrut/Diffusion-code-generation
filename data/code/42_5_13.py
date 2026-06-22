import math

def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    major_axis_sample = 10
    minor_axis_sample = 6
    area = calculate_ellipse_area(major_axis_sample, minor_axis_sample)
    print(area)