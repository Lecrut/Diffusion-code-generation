def generate_sequence(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    return (3 * i - 2 for i in range(1, n + 1))

if __name__ == '__main__':
    N = 10
    sequence = list(generate_sequence(N))
    print(sequence)