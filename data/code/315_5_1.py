def generate_repeating_sequence(N):
    if N <= 0:
        return []
    pattern_length = 3
    sequence = []
    for i in range(N):
        sequence.append((i % pattern_length) + 1)
    return sequence
if __name__ == '__main__':
    N_terms = 20
    result = generate_repeating_sequence(N_terms)
    print(result)