def validate_triangles(triplets):
    results = []
    for a, b, c in triplets:
        is_valid = (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0)
        results.append(is_valid)
    return results

if __name__ == '__main__':
    sample_triplets = [(3, 4, 5), (1, 2, 10), (5, 5, 5), (0, 1, 2), (2, 2, 3)]
    print(validate_triangles(sample_triplets))