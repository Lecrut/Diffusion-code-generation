def generate_geometric_sequence(a, r, n):
    current = a
    for _ in range(n):
        yield current
        current *= r
if __name__ == '__main__':
    first_term = 2
    common_ratio = 3
    num_terms = 5
    sequence_generator = generate_geometric_sequence(first_term, common_ratio, num_terms)
    result = list(sequence_generator)
    print(result)