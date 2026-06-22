def generate_sequence(n):
    return (3 * i - 2 for i in range(1, n + 1))

if __name__ == '__main__':
    N = 10
    sequence_values = list(generate_sequence(N))
    print(sequence_values)