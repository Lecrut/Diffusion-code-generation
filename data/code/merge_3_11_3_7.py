def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length_b == 0:
        # Handle division by zero gracefully without printing an error message to stdout
        return
    
    ratio = length_a / length_b
    print(f"Ratio ({length_a} : {length_b}) = {ratio}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no user input, args, or network access)
    sample_length_1 = 10.5
    sample_length_2 = 3
    
    calculate_ratio(sample_length_1, sample_length_2)

    # Test the division by zero handling case with pre-defined value for length_b being zero
    test_sample_1 = 8.7
    test_sample_2 = 0.0
    
    calculate_ratio(test_sample_1, test_sample_2)