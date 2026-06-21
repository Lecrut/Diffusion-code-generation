import math

def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        raise ValueError('At least three points are required to form a convex hull.')
    coordinates.sort(key=lambda p: (p[0], p[1]))

    def shoelace_formula(points):
        area = 0.0
        j = n - 1
        for i in range(n):
            area += (points[j][0] + points[i][0]) * (points[j][1] - points[i][1])
            j = i
        return abs(area) / 2.0
    return shoelace_formula(coordinates)
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    area = calculate_area_of_convex_hull(sample_coordinates)
    print(area)