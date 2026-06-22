import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def triangle_sides_length(point1, point2, point3):
    side1 = calculate_distance(point1, point2)
    side2 = calculate_distance(point2, point3)
    side3 = calculate_distance(point3, point1)
    return side1, side2, side3

if __name__ == '__main__':
    pointA = (0, 0)
    pointB = (3, 4)
    pointC = (6, 0)
    
    sides = triangle_sides_length(pointA, pointB, pointC)
    print(sides)