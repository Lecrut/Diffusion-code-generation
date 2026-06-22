def generate_fibonacci_sequence(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    sequence = [0, 1]
    while len(sequence) <= n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence[:n + 1]

if __name__ == '__main__':
    result = generate_fibonacci_sequence(1000)
    print(result[-1])