def generate_square_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.append(i ** 2)
    return sequence

if __name__ == '__main__':
    sample_size = 5
    result = generate_square_sequence(sample_size)
    print(result)