def generate_geometric_sequence(iterations):
    if not isinstance(iterations, int) or iterations < 0:
        raise ValueError("Iterations must be a non-negative integer")
    
    sequence = [1]
    for _ in range(iterations):
        sequence.append(sequence[-1] * 3)
    return sequence

if __name__ == '__main__':
    try:
        print(generate_geometric_sequence(8))
    except ValueError as e:
        print(e)