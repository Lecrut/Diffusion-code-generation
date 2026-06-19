def find_middle_index(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or a tuple.")
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty.")
    
    length = len(sequence)
    middle_index = (length - 1) // 2
    return middle_index

if __name__ == '__main__':
    try:
        sample_sequence_odd = [1, 2, 3, 4, 5]
        sample_sequence_even = [1, 2, 3, 4, 5, 6]
        empty_sequence = []
        
        print(find_middle_index(sample_sequence_odd))  # Output: 2
        print(find_middle_index(sample_sequence_even)) # Output: 2
        
        # Uncomment the following line to see exception handling in action
        # print(find_middle_index(empty_sequence))    # Raises ValueError
    except Exception as e:
        print(f"An error occurred: {e}")