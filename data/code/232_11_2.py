def generate_growing_sequence(start, factor):
    sequence = []
    current_term = start
    for _ in range(10):
        sequence.append(current_term)
        current_term *= factor
    for i, term in enumerate(sequence):
        print(f"Term {i+1}: {term}")
if __name__ == '__main__':
    generate_growing_sequence(2, 3)