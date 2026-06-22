def find_middle_index(sequence):
    length = len(sequence)
    if length % 2 == 0:
        # For even length, return the first middle index
        return length // 2 - 1
    else:
        # For odd length, return the single middle index
        return length // 2

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4]

    middle_index_odd = find_middle_index(sample_sequence_odd)
    middle_index_even = find_middle_index(sample_sequence_even)

    print("Middle index of odd sequence:", middle_index_odd)
    print("Middle index of even sequence:", middle_index_even)