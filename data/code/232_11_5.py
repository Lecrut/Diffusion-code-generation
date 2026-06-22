def generate_growing_sequence(start=1, factor=2):
    sequence = [start]
    for _ in range(1, 5):
        next_term = sequence[-1] * factor
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_growing_sequence()
    for term in sample_sequence:
        print(term)