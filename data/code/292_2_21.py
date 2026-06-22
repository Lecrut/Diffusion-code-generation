import math
SEMI_PERIMETER_FACTOR = 0.5

def triangle_perimeter(a, b, c):
    s = (a + b + c) * SEMI_PERIMETER_FACTOR
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
if __name__ == '__main__':
    print(triangle_perimeter(3, 4, 5))