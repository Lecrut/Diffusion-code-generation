def find_peak(sequence):
    return max(sequence)

if __name__ == '__main__':
    sample_sequence = [7, 10, 2, 3, 45, 8]
    peak_value = find_peak(sample_sequence)
    print(peak_value)