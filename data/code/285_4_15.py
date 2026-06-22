def compare_consecutive_elements(sequence):
    return ['increasing' if b > a else 'decreasing' if b < a else 'equal' for a, b in zip(sequence, sequence[1:])]

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 2, 1]
    print(compare_consecutive_elements(sample_sequence))