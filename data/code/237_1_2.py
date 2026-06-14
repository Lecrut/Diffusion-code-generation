def generate_geometric_sequence(a, r, n):
    current_term = a
    for _ in range(n):
        yield current_term
        current_term *= r
if __name__ == '__main__':
    first_term = 2
    common_ratio = 3
    num_terms = 5
    sequence = generate_geometric_sequence(first_term, common_ratio, num_terms)
    result_list = list(sequence)
    print(result_list)