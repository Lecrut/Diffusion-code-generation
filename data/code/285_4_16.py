def compare_consecutive_elements(sequence):
    return ['increasing' if a < b else 'decreasing' if a > b else 'equal' for a, b in zip(sequence, sequence[1:])]

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 7, 9]
    print(compare_consecutive_elements(sample_sequence))