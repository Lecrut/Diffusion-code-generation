def generate_geometric_sequence():
    sequence = [1]
    multiplier = 3
    iterations = 8
    for _ in range(iterations):
        sequence.append(sequence[-1] * multiplier)
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_geometric_sequence()
    print(sample_sequence)