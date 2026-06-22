def generate_geometric_sequence():
    sequence = [1]
    try:
        for _ in range(8):
            sequence.append(sequence[-1] * 3)
    except Exception as e:
        raise ValueError("Failed to generate geometric sequence") from e
    return sequence

if __name__ == '__main__':
    print(generate_geometric_sequence())