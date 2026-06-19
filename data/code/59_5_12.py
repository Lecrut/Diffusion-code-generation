def calculate_middle_index(sequence):
    length = len(sequence)
    middle_index = length // 2
    return middle_index - 1 if length % 2 == 0 else middle_index

if __name__ == '__main__':
    sample_sequence_odd = [1.5, 2.5, 3.5, 4.5, 5.5]
    sample_sequence_even = [10.5, 20.5, 30.5, 40.5, 50.5, 60.5]
    sample_sequence_single = [7.0]
    
    print(calculate_middle_index(sample_sequence_odd))  # Output: 2
    print(calculate_middle_index(sample_sequence_even)) # Output: 2
    print(calculate_middle_index(sample_sequence_single)) # Output: 0