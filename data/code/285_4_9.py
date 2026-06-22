def compare_consecutive_elements(sequence):
    return ['increasing' if sequence[i] < sequence[i+1] else 'decreasing' if sequence[i] > sequence[i+1] else 'equal' for i in range(len(sequence)-1)]

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 7]
    print(compare_consecutive_elements(sample_sequence))