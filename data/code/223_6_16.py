def find_peak(sequence):
    return max(sequence)

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 1]
    peak_value = find_peak(sample_sequence)
    print(peak_value)