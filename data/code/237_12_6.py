def generate_geometric_sequence():
    sequence = [1]
    multiplier = 3
    for _ in range(8):
        sequence.append(sequence[-1] * multiplier)
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_geometric_sequence()
    print(sample_sequence)