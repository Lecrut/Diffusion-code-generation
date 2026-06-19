def find_middle_index(sequence):
    length = len(sequence)
    middle_index = (length - 1) // 2
    return middle_index

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]

    print(find_middle_index(sample_sequence_odd))  # Output: 2
    print(find_middle_index(sample_sequence_even)) # Output: 2