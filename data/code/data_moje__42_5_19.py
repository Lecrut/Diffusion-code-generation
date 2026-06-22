import math

def compute_ellipse_area(major, minor):
    if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
        raise TypeError("Axes must be numeric")
    if major <= 0 or minor <= 0:
        raise ValueError("Axes must be positive")
    semi_major = major * 0.5
    semi_minor = minor * 0.5
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    MAJOR = 20
    MINOR = 10
    result = compute_ellipse_area(MAJOR, MINOR)
    print(result)