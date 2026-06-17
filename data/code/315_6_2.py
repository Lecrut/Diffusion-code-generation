def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    return sequence
if __name__ == '__main__':
    cycle_length = 10
    fib_sequence = generate_fibonacci_sequence(cycle_length)
    print(*fib_sequence)