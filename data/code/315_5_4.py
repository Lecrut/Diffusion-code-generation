def generate_repeating_sequence(N):
    if N <= 0:
        return []
    pattern_length = 3
    sequence = []
    for i in range(N):
        index = i % pattern_length
        value = index + 1
        sequence.append(value)
    return sequence
if __name__ == '__main__':
    N_terms = 15
    result = generate_repeating_sequence(N_terms)
    print(result)