def generate_sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        next_term = sum(sequence[-2:]) + 1
        sequence.append(next_term)
    return sequence

if __name__ == '__main__':
    sample_values = 10
    result = generate_sequence(sample_values)
    print(result)