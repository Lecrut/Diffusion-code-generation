def get_center_element(sequence):
    sequence_length = len(sequence)
    center_index = (sequence_length - 1) // 2
    return sequence[center_index]

if __name__ == '__main__':
    sample_sequence = [7, 3, 1, 8, 4, 9]
    print(get_center_element(sample_sequence))