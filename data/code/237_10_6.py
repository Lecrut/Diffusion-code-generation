def fibonacci_sequence(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    sequence = [0, 1]
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence[:n]

if __name__ == '__main__':
    print(fibonacci_sequence(20))