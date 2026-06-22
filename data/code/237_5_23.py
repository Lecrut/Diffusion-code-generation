def generate_sequence(n):
    if n < 1:
        raise ValueError("n must be at least 1")
    return [i**2 + i for i in range(1, n+1)]

if __name__ == '__main__':
    sample_n = 10
    sequence = generate_sequence(sample_n)
    print(sequence)