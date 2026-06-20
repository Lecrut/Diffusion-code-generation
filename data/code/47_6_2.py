import math

def triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    return area

if __name__ == '__main__':
    result = triangle_area(0, 0, 4, 0, 0, 3)
    print(result)