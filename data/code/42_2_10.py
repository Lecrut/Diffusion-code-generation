import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    result = calculate_ellipse_area(5, 3)
    print(result)