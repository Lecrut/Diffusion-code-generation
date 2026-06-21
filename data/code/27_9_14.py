def validate_triangles(triplets):
    return [all(side > 0 and (a + b > c) and (a + c > b) and (b + c > a) for a, b, c in [(x, y, z)]) for x, y, z in triplets]

if __name__ == '__main__':
    sample_triplets = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (10, 2, 1),
        (6, 6, 6)
    ]
    results = validate_triangles(sample_triplets)
    for result in results:
        print(result)