def validate_triangle_inequalities(triplets):
    return [all(2 * x < sum(triplet) for x in triplet) for triplet in triplets]

if __name__ == '__main__':
    sample_triplets = [[3, 4, 5], [1, 2, 3], [10, 5, 2], [7, 7, 7], [1, 1, 3]]
    results = validate_triangle_inequalities(sample_triplets)
    for result in results:
        print(result)