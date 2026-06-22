def generate_fibonacci_sequence(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

if __name__ == '__main__':
    index_limit = 1000
    fib_sequence = generate_fibonacci_sequence(index_limit)
    print(len(fib_sequence))
    print(fib_sequence[-1])