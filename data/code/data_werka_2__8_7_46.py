def calculate_convex_hull_area(coordinates):

    def shoelace_formula(coords):
        n = len(coords)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += coords[i][0] * coords[j][1]
            area -= coords[j][0] * coords[i][1]
        return abs(area) / 2.0
    if len(coordinates) < 3:
        raise ValueError('At least three points are required to form a convex hull.')
    coordinates.sort(key=lambda x: (x[0], x[1]))
    lower_hull = []
    for point in coordinates:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)
    upper_hull = []
    for point in reversed(coordinates):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)
    convex_hull = lower_hull[:-1] + upper_hull[:-1]
    return shoelace_formula(convex_hull)

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)