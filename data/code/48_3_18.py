import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def triangle_side_lengths(point1, point2, point3):
    side1 = calculate_distance(point1, point2)
    side2 = calculate_distance(point2, point3)
    side3 = calculate_distance(point3, point1)
    return side1, side2, side3

if __name__ == '__main__':
    points = {
        'A': (0, 0),
        'B': (4, 0),
        'C': (0, 3)
    }
    
    side_lengths = triangle_side_lengths(points['A'], points['B'], points['C'])
    print(f"Side lengths of the triangle: {side_lengths}")