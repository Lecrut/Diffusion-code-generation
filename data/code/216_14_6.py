def find_central_element(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    length = len(sequence)
    central_index = (length - 1) // 2
    return sequence[central_index]

if __name__ == '__main__':
    sample_sequence = [7, 3, 1, 8, 4, 9]
    print(find_central_element(sample_sequence))