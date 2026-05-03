import math
if __name__ == '__main__':
    vertices = [
        (0, 0),
        (3, 0),
        (3, 4),
        (0, 4)
    ]
    perimeter = 0.0
    num_vertices = len(vertices)
    for i in range(num_vertices):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % num_vertices]
        x1, y1 = p1
        x2, y2 = p2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    print(perimeter)