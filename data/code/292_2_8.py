import math
EPSILON = 1e-09

def triangle_perimeter(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    perimeter = triangle_perimeter(side1, side2, side3)
    print(perimeter)