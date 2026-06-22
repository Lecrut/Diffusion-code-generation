import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    result = ellipse_area(5, 3)
    print(result)