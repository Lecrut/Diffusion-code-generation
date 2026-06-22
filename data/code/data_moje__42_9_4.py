import math

def area_of_ellipse(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a = 5
    b = 3
    result = area_of_ellipse(a, b)
    print(result)