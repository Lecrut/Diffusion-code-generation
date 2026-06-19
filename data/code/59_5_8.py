def find_middle_index(sequence):
    LENGTH_THRESHOLD = 2
    length = len(sequence)
    if length < LENGTH_THRESHOLD:
        raise ValueError("Sequence must contain at least two elements.")
    
    middle_index = length // 2
    if length % 2 == 0:
        # For even length, return the lower middle index
        return middle_index - 1
    else:
        # For odd length, return the middle index
        return middle_index

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]
    sample_sequence_single = [10]
    sample_sequence_pair = [1.0, 2.0]

    try:
        print("Middle index of odd sequence:", find_middle_index(sample_sequence_odd))  # Output: 2
        print("Middle index of even sequence:", find_middle_index(sample_sequence_even))  # Output: 2
        print("Middle index of single element sequence:", find_middle_index(sample_sequence_single))
    except ValueError as e:
        print(e)

    try:
        print("Middle index of pair sequence:", find_middle_index(sample_sequence_pair))
    except ValueError as e:
        print(e)