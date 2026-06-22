def generate_growing_sequence(start, factor, iterations):
    sequence = []
    current_term = start
    for _ in range(iterations):
        sequence.append(current_term)
        current_term *= factor
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_growing_sequence(1, 2, 5)
    for term in sample_sequence:
        print(term)