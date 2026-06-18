def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length_b == 0:
        print("Error: Division by zero is undefined.")
        return
    
    ratio = length_a / length_b
    print(f"The ratio of {length_a} to {length_b} is {ratio}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input() or prompts)
    sample_length_1: float = 20.5
    sample_length_2: float = 4
    
    calculate_ratio(sample_length_1, sample_length_2)

if __name__ == '__main__':
    # Test case for division by zero (commented out to prevent accidental execution in some environments if copy-pasted incorrectly, 
    # but logically part of the module's test suite structure. Since we cannot use input(), this is a static check).
    sample_length_3: float = 10
    sample_length_4: float = 0
    
    calculate_ratio(sample_length_3, sample_length_4)