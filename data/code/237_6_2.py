def generate_fibonacci(n):
    sequence = [0, 1]
    if n <= 2:
        if n >= 1:
            return sequence[:n]
        else:
            return []
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence
if __name__ == '__main__':
    n = 12
    result = generate_fibonacci(n)
    print(*result)