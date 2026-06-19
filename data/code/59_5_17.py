def find_middle_index(sequence):
    length = len(sequence)
    if length % 2 == 0:
        return length // 2 - 1
    else:
        return length // 2

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]

    middle_index_odd = find_middle_index(sample_sequence_odd)
    middle_index_even = find_middle_index(sample_sequence_even)

    print(f"Middle index of odd sequence: {middle_index_odd}")
    print(f"Middle index of even sequence: {middle_index_even}")