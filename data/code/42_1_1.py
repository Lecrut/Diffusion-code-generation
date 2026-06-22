import math

def compute_ellipse_area(major_axis, minor_axis):
    semi_major = major_axis / 2.0
    semi_minor = minor_axis / 2.0
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major_dimensions = [10.0, 20.5, 50.0]
    minor_dimensions = [5.0, 10.25, 25.0]
    
    results = []
    for i in range(len(major_dimensions)):
        area = compute_ellipse_area(major_dimensions[i], minor_dimensions[i])
        results.append(area)
        print(area)