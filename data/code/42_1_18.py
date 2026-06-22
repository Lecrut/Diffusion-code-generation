import math

def compute_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError("Axis dimensions must be positive.")
    return math.pi * (major_axis / 2) * (minor_axis / 2)

if __name__ == '__main__':
    sample_major = 10.5
    sample_minor = 7.3
    result = compute_ellipse_area(sample_major, sample_minor)
    print(result)