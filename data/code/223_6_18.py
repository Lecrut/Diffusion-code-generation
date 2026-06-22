MAX_SEQUENCE_LENGTH = 100

def find_peak(sequence):
    if len(sequence) > MAX_SEQUENCE_LENGTH:
        raise ValueError("Sequence too long")
    return max(sequence)

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 1]
    peak_value = find_peak(sample_sequence)
    print(peak_value)