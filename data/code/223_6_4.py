def find_peak(sequence):
    return max(sequence)

if __name__ == '__main__':
    sample_sequence = [10, 3.14, 5, 22.9, -1.5]
    peak_value = find_peak(sample_sequence)
    print(peak_value)