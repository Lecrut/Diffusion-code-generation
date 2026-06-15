def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence
if __name__ == '__main__':
    n = 12
    fib_sequence = generate_fibonacci(n)
    print(*fib_sequence)