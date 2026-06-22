def generate_growing_sequence(iterations):
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError("Iterations must be a positive integer.")
    
    sequence = []
    current_term = 1
    for _ in range(iterations):
        sequence.append(current_term)
        current_term *= 2
    
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_growing_sequence(5)
    print(sample_sequence)