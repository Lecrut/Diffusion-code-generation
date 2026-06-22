import numpy as np

def calculate_polygon_area(vertices):
    if not all((isinstance(v, tuple) and len(v) == 2 for v in vertices)):
        raise ValueError('Vertices must be a list of (x, y) tuples')
    num_vertices = len(vertices)
    area = 0.5 * np.abs(np.dot(np.array([v[0] for v in vertices + vertices[:1]]), np.roll(np.array([v[1] for v in vertices + vertices[:1]]), -1)))
    return area

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError('Radius must be a positive number')
    return np.pi * radius ** 2
if __name__ == '__main__':
    polygon_vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
    circle_radius = 1.5
    polygon_area = calculate_polygon_area(polygon_vertices)
    circle_area = calculate_circle_area(circle_radius)
    print(f'Polygon area: {polygon_area}')
    print(f'Circle area: {circle_area}')