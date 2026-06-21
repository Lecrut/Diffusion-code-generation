def validate_triangles(triplets):
    return [all(sorted([a, b, c])[:2] > [a, b, c][2] for a, b, c in [triplet]) and all(x > 0 for x in triplet) for triplet in triplets]

if __name__ == '__main__':
    triplets = [(3, 4, 5), (1, 2, 3), (5, 12, 13), (1, 1, 10), (0, 5, 5), (10, 10, 10)]
    results = validate_triangles(triplets)
    print(results)