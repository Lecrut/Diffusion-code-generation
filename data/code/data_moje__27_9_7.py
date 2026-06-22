def validate_triangles(triplets):
    return [a + b > c and a + c > b and b + c > a for a, b, c in triplets]

if __name__ == '__main__':
    sample_triplets = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (1, 1, 1),
        (10, 2, 3)
    ]
    print(validate_triangles(sample_triplets))