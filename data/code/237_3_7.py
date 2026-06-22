def generate_geometric_sequence(start, ratio, terms):
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term *= ratio
    return sequence

if __name__ == '__main__':
    initial_value = 5
    step_factor = 3
    num_terms = 8
    output_sequence = generate_geometric_sequence(initial_value, step_factor, num_terms)
    print(output_sequence)