import math

def calculate_triangle_vertices(center_x, center_y, radius):
    angle_step = 2 * math.pi / 3
    vertices = []
    
    for i in range(3):
        angle = i * angle_step
        vertex_x = center_x + radius * math.cos(angle)
        vertex_y = center_y + radius * math.sin(angle)
        vertices.append((vertex_x, vertex_y))
    
    return vertices

if __name__ == '__main__':
    try:
        center_x, center_y = 0, 0
        radius = 5
        if radius <= 0:
            raise ValueError("Radius must be greater than zero")
        
        vertices = calculate_triangle_vertices(center_x, center_y, radius)
        print(vertices)
    except ValueError as e:
        print(e)