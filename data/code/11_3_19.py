def calculate_ratio(length1: float, length2: float) -> None:
    """Calculates and prints the ratio of two lengths."""
    if length2 == 0:
        print("Error: Division by zero is not possible.")
        return
    
    ratio = length1 / length2
    print(f"The ratio of {length1} to {length2} is {ratio}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used here.
    sample_length_1 = 10.5
    sample_length_2 = 3
    
    calculate_ratio(sample_length_1, sample_length_2)

    # Testing the division by zero handling with a second set of values where length2 is zero.
    test_sample_length_1 = 5
    test_sample_length_2 = 0
    calculate_ratio(test_sample_length_1, test_sample_length_2)