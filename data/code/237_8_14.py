def generate_sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        next_term = sum(sequence[-2:]) + 1
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    sample_terms = generate_sequence(10)
    print(sample_terms)