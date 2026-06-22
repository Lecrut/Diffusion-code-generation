MAX_SEQUENCE_LENGTH = 100

def find_peak(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    if len(sequence) > MAX_SEQUENCE_LENGTH:
        raise ValueError(f"Sequence length exceeds maximum allowed ({MAX_SEQUENCE_LENGTH})")
    return max(sequence)

if __name__ == '__main__':
    sample_sequence = [3, 5, 2, 8, 1]
    print(find_peak(sample_sequence))