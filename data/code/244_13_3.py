import math

def ellipse_area(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Semi-major and semi-minor axes must be numbers")
    return math.pi * a * b

if __name__ == '__main__':
    area1 = ellipse_area(3, 4)
    area2 = ellipse_area(5, 6)
    total_area = area1 + area2
    print(total_area)