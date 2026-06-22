import math

def calculate_area_of_convex_hull(coordinates):
    def shoelace_formula(coords):
        n = len(coords)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += coords[i][0] * coords[j][1]
            area -= coords[j][0] * coords[i][1]
        return abs(area) / 2.0

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def convex_hull(coords):
        n = len(coords)
        if n < 3:
            return []

        l = 0
        for i in range(1, n):
            if coords[i][0] < coords[l][0]:
                l = i

        hull = []
        p = l
        q = 0
        while True:
            hull.append(coords[p])
            q = (p + 1) % n
            for i in range(n):
                if orientation(coords[p], coords[i], coords[q]) == 2:
                    q = i

            p = q

            if p == l:
                break

        return hull

    hull_points = convex_hull(coordinates)
    return shoelace_formula(hull_points)

if __name__ == '__main__':
    sample_coordinates = [
        (0, 3),
        (2, 2),
        (5, 1),
        (6, 4),
        (4, 0),
        (3, 3)
    ]
    area = calculate_area_of_convex_hull(sample_coordinates)
    print(area)