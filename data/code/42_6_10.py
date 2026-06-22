import math

def area_of_ellipse(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    result = area_of_ellipse(5.0, 3.0)
    print(result)