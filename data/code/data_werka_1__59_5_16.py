def calculate_middle_index(sequence):
    length = len(sequence)
    return (length - 1) // 2

if __name__ == '__main__':
    sample_odd = [1.0, 2.0, 3.0, 4.0, 5.0]
    sample_even = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sample_single = [7.0]
    sample_pair = [8.0, 9.0]

    print(calculate_middle_index(sample_odd))  # Output: 2
    print(calculate_middle_index(sample_even)) # Output: 2
    print(calculate_middle_index(sample_single)) # Output: 0
    print(calculate_middle_index(sample_pair))   # Output: 0