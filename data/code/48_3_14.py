import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def triangle_sides_length(p1, p2, p3):
    side1 = calculate_distance(p1, p2)
    side2 = calculate_distance(p2, p3)
    side3 = calculate_distance(p3, p1)
    return side1, side2, side3

if __name__ == '__main__':
    points = {
        'A': (0, 0),
        'B': (3, 4),
        'C': (6, 0)
    }
    
    side_lengths = triangle_sides_length(points['A'], points['B'], points['C'])
    print(f"Sides of the triangle: {side_lengths}")