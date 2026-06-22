def generate_growing_sequence(start, factor):
    sequence = []
    current_term = start
    for _ in range(10):
        sequence.append(current_term)
        current_term *= factor
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_growing_sequence(1, 2)
    for term in sample_sequence[:5]:
        print(term)