import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def triangle_side_lengths(point1, point2, point3):
    side1 = calculate_distance(point1, point2)
    side2 = calculate_distance(point2, point3)
    side3 = calculate_distance(point3, point1)
    return side1, side2, side3

if __name__ == '__main__':
    pointA = (0, 0)
    pointB = (3, 4)
    pointC = (6, 8)
    
    sides = triangle_side_lengths(pointA, pointB, pointC)
    print(sides)