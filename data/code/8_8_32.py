import numpy as np

def calculate_convex_hull_area(points):

    def shoelace_formula(coords):
        n = len(coords)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += coords[i][0] * coords[j][1]
            area -= coords[j][0] * coords[i][1]
        return abs(area) / 2.0
    points_array = np.array(points)
    from scipy.spatial import ConvexHull
    hull = ConvexHull(points_array)
    hull_points = points_array[hull.vertices]
    return shoelace_formula(hull_points)
if __name__ == '__main__':
    sample_points = [(0, 0), (4, 0), (4, 3), (0, 3), (1, 2)]
    area = calculate_convex_hull_area(sample_points)
    print(area)