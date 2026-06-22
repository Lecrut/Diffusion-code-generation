def generate_square_sequence(limit):
    sequence = []
    for i in range(limit):
        sequence.append(i**2)
    return sequence

if __name__ == '__main__':
    sample_limit = 10
    square_sequence = generate_square_sequence(sample_limit)
    print(square_sequence)