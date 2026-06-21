def determine_triangle_validity(side_sets):
    return [sorted(sides)[:2][0] + sorted(sides)[:2][1] > sorted(sides)[2] and all(side > 0 for side in sides) for sides in side_sets]

if __name__ == '__main__':
    sample_side_sets = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 10, 10),
        (1, 1, 100),
        (5, 12, 13),
        (7, 24, 25),
        (0, 5, 5),
        (-1, 2, 3),
        (1, 1, 1),
        (6, 6, 6)
    ]
    print(determine_triangle_validity(sample_side_sets))