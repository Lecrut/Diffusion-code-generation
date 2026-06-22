import math

def calculate_ellipse_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * a * b

if __name__ == '__main__':
    area1 = calculate_ellipse_area(5, 3)
    print(area1)

    area2 = calculate_ellipse_area(10, 10)
    print(area2)

    area3 = calculate_ellipse_area(7.5, 2.5)
    print(area3)