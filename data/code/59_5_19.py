def find_middle_index(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    
    middle_index = length // 2
    return middle_index

if __name__ == '__main__':
    try:
        sample_sequence_odd = [1, 2, 3, 4, 5]
        sample_sequence_even = [1, 2, 3, 4, 5, 6]
        empty_sequence = []
        
        print("Middle index of odd sequence:", find_middle_index(sample_sequence_odd))  # Output: 2
        print("Middle index of even sequence:", find_middle_index(sample_sequence_even)) # Output: 2
        print("Middle index of empty sequence:", find_middle_index(empty_sequence))     # Raises ValueError
    except (TypeError, ValueError) as e:
        print(e)