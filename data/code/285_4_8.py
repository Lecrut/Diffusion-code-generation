def compare_consecutive(sequence):
    return ['increasing' if b > a else 'decreasing' if b < a else 'equal' for a, b in zip(sequence, sequence[1:])]

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 7, 9]
    print(compare_consecutive(sample_sequence))