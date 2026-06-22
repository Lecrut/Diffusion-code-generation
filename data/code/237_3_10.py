def generate_geometric_sequence(start, ratio):
    sequence = []
    for _ in range(8):
        sequence.append(start)
        start *= ratio
    return sequence

if __name__ == '__main__':
    initial_value = 5
    multiplier = 3
    sample_result = generate_geometric_sequence(initial_value, multiplier)
    print(sample_result)