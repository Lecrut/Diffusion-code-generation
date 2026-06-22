def is_valid_sequence(sequence):
    if not isinstance(sequence, list) or not all(isinstance(item, int) for item in sequence):
        raise ValueError("Input must be a list of integers")

def find_central_element(sequence):
    is_valid_sequence(sequence)
    length = len(sequence)
    central_index = (length - 1) // 2
    return sequence[central_index]

if __name__ == '__main__':
    sample_sequence = [7, 3, 1, 8, 4, 9]
    print(find_central_element(sample_sequence))