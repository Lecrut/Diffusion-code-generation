import math

def compute_ellipse_area(major_axis, minor_axis):
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    major_axes = [10, 20, 5.5, 100]
    minor_axes = [5, 10, 2.2, 50]
    
    for major, minor in zip(major_axes, minor_axes):
        area = compute_ellipse_area(major, minor)
        print(area)