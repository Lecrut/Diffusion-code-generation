def validate_triangles(triplets):
    return [all(triangle[i] < sum(triangle) / 2 for i in range(3)) for triangle in triplets]

if __name__ == '__main__':
    sample_triplets = [
        (3, 4, 5),
        (1, 2, 10),
        (5, 5, 5),
        (7, 10, 2),
        (9, 12, 15)
    ]
    results = validate_triangles(sample_triplets)
    for result in results:
        print(result)