def generate_geometric_sequence(start=1, factor=3, iterations=8):
    sequence = [start]
    for _ in range(1, iterations):
        next_value = sequence[-1] * factor
        sequence.append(next_value)
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_geometric_sequence(start=2, factor=5, iterations=6)
    print(sample_sequence)