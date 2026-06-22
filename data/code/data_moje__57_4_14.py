def get_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

if __name__ == '__main__':
    limit = 200
    result = get_fibonacci_sequence(limit)
    print(result)