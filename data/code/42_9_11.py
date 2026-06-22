import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a = 5
    b = 3
    result = ellipse_area(a, b)
    print(result)