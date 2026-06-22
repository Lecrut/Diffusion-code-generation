def compare_consecutive_elements(sequence):
    return ['increasing' if x < y else 'decreasing' if x > y else 'equal' for x, y in zip(sequence, sequence[1:])]

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 6, 7]
    print(compare_consecutive_elements(sample_sequence))