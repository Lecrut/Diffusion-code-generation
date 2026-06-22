def generate_fibonacci_sequence(limit):
    sequence = [0, 1]
    for i in range(2, limit + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci_sequence(1000)
    print(result[-1])