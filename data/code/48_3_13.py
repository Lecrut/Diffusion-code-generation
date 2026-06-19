import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def triangle_sides_length(p1, p2, p3):
    side1 = calculate_distance(p1, p2)
    side2 = calculate_distance(p2, p3)
    side3 = calculate_distance(p3, p1)
    return side1, side2, side3

if __name__ == '__main__':
    point1 = (0, 0)
    point2 = (3, 4)
    point3 = (6, 8)
    
    sides = triangle_sides_length(point1, point2, point3)
    print(sides)