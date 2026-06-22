def generate_geometric_sequence():
    sequence = [1]
    if len(sequence) < 8:
        for _ in range(7):
            sequence.append(sequence[-1] * 3)
    return sequence

if __name__ == '__main__':
    print(generate_geometric_sequence())