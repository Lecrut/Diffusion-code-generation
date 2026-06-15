def generate_geometric_sequence(a, r, n):
    sequence = []
    for i in range(n):
        term = a * (r ** i)
        sequence.append(term)
    return sequence
if __name__ == '__main__':
    first_term = 2
    common_ratio = 3
    num_terms = 5
    result = generate_geometric_sequence(first_term, common_ratio, num_terms)
    print(result)