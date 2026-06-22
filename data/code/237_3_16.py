def generate_geometric_sequence(start_value, ratio, terms):
    sequence = []
    for _ in range(terms):
        sequence.append(start_value)
        start_value *= ratio
    return sequence

if __name__ == '__main__':
    sample_sequence = generate_geometric_sequence(5, 3, 8)
    print(sample_sequence)