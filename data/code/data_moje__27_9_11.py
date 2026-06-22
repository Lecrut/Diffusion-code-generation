def validate_triangle_inequality(triplets):
    return [a + b > c and a + c > b and b + c > a for a, b, c in triplets]

if __name__ == '__main__':
    sample_triplets = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 20, 25),
        (5, 5, 10),
        (1, 10, 12),
        (7, 24, 25)
    ]
    results = validate_triangle_inequality(sample_triplets)
    for result in results:
        print(result)