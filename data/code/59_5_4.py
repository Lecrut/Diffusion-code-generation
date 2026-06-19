def find_middle_index(sequence):
    sequence_length = len(sequence)
    if sequence_length % 2 == 0:
        # Even length, return the lower middle index
        middle_index = (sequence_length // 2) - 1
    else:
        # Odd length, return the single middle index
        middle_index = sequence_length // 2
    return middle_index

if __name__ == '__main__':
    sample_sequence_odd = [7, 8, 9, 10, 11]
    sample_sequence_even = [1, 3, 5, 7, 9, 11]
    
    odd_middle_index = find_middle_index(sample_sequence_odd)
    even_middle_index = find_middle_index(sample_sequence_even)
    
    print("Middle index of odd sequence:", odd_middle_index)  # Output: 2
    print("Middle index of even sequence:", even_middle_index)  # Output: 2