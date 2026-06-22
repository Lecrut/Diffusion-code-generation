def generate_lucas(n):
    sequence = [2, 1]
    if n <= 2:
        return sequence[:n]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    n_terms = 9
    lucas_sequence = generate_lucas(n_terms)
    print(*lucas_sequence)