import math

def calculate_triangle_vertices(center_x, center_y, radius):
    angle_step = 2 * math.pi / 3
    vertices = []
    for i in range(3):
        angle = i * angle_step
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        vertices.append((x, y))
    return vertices

if __name__ == '__main__':
    center_x = 0
    center_y = 0
    radius = 1
    vertices = calculate_triangle_vertices(center_x, center_y, radius)
    print(vertices)