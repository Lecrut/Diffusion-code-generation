import math

def compute_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major_values = [10.0, 25.5, 100.0, 5.123456]
    minor_values = [4.0, 8.3, 25.0, 2.123456]
    for i in range(len(major_values)):
        area = compute_ellipse_area(major_values[i], minor_values[i])
        print(f"Area for axes {major_values[i]} and {minor_values[i]}: {area}")