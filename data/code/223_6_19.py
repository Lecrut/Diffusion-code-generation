def find_peak(sequence):
    return max(sequence)

if __name__ == '__main__':
    sample_sequence = [12, 45, 78, 3, 90]
    peak_value = find_peak(sample_sequence)
    print(peak_value)