def generate_geometric_sequence():
    if not isinstance(8, int) or 8 <= 0:
        raise ValueError("Iterations must be a positive integer")
    
    sequence = [1]
    for _ in range(7):
        sequence.append(sequence[-1] * 3)
    return sequence

if __name__ == '__main__':
    print(generate_geometric_sequence())