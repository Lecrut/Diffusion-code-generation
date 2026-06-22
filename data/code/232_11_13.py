def generate_growing_sequence(max_iterations):
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError("max_iterations must be a positive integer")
    
    current_term = 1
    for _ in range(max_iterations):
        yield current_term
        current_term *= 2

if __name__ == '__main__':
    sequence_generator = generate_growing_sequence(5)
    for term in sequence_generator:
        print(term)