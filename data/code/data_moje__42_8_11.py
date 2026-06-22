import math

def calculate_ellipse_area():
    a = 5.0
    b = 3.0
    area = math.pi * a * b
    return area

if __name__ == '__main__':
    result = calculate_ellipse_area()
    print(result)