def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0

    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]

    return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    print(calculate_area_of_convex_hull(sample_coordinates))