import math

def compute_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis dimensions must be positive numbers")
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    major_dim = 10.5
    minor_dim = 6.3
    area = compute_ellipse_area(major_dim, minor_dim)
    print(area)