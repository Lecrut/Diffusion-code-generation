def generate_lucas(n):
    if n <= 0:
        return []
    elif n == 1:
        return [2]
    lucas_sequence = [2, 1]
    for i in range(2, n):
        next_term = lucas_sequence[-1] + lucas_sequence[-2]
        lucas_sequence.append(next_term)
    return lucas_sequence

if __name__ == '__main__':
    n_terms = 9
    lucas_sequence = generate_lucas(n_terms)
    print(*lucas_sequence)