import numpy as np

def shoelace_formula(coords):
    n = len(coords)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    return abs(area) / 2.0

def convex_hull_area(coords):
    hull = np.convex_hull(np.array(coords))
    hull_coords = [(coords[hull.vertices[i]][0], coords[hull.vertices[i]][1]) for i in range(len(hull.vertices))]
    return shoelace_formula(hull_coords)

if __name__ == '__main__':
    sample_coords = [
        (34.0522, -118.2437),
        (40.7128, -74.0060),
        (37.7749, -122.4194),
        (47.6062, -122.3321)
    ]
    area = convex_hull_area(sample_coords)
    print(area)