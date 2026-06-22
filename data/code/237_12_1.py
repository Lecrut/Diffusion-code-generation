def generate_geometric_sequence():
    sequence = [1]
    for _ in range(1, 8):
        sequence.append(sequence[-1] * 3)
    return sequence

if __name__ == '__main__':
    print(generate_geometric_sequence())