LUCAS_0 = 2
LUCAS_1 = 1

def generate_lucas_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [LUCAS_0]
    sequence = [LUCAS_0, LUCAS_1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    n_terms = 9
    lucas_sequence = generate_lucas_sequence(n_terms)
    print(*lucas_sequence)