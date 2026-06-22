def compare_consecutive_elements(sequence):
    return ['increasing' if sequence[i] < sequence[i+1] else 'decreasing' if sequence[i] > sequence[i+1] else 'equal' for i in range(len(sequence)-1)]

if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 4, 5, 5]
    print(compare_consecutive_elements(sample_sequence))