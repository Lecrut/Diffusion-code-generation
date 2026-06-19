import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def triangle_sides_length(p1, p2, p3):
    side1 = distance(p1, p2)
    side2 = distance(p2, p3)
    side3 = distance(p3, p1)
    return side1, side2, side3

if __name__ == '__main__':
    pointA = (0, 0)
    pointB = (4, 0)
    pointC = (0, 3)

    side1, side2, side3 = triangle_sides_length(pointA, pointB, pointC)
    print(f"Side 1: {side1}")
    print(f"Side 2: {side2}")
    print(f"Side 3: {side3}")