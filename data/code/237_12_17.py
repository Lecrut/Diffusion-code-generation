def generate_geometric_sequence(start=1, multiplier=3, iterations=8):
    sequence = [start]
    for _ in range(iterations - 1):
        next_value = sequence[-1] * multiplier
        sequence.append(next_value)
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_geometric_sequence(2, 5, 4)
    print(sample_sequence)