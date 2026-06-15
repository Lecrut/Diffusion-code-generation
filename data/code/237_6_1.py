def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
        return sequence
if __name__ == '__main__':
    n_terms = 12
    fib_sequence = generate_fibonacci_sequence(n_terms)
    print(*fib_sequence)