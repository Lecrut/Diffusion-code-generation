def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculates and prints the ratio of two lengths."""
    if length_b == 0:
        print("Error: Division by zero is undefined.")
        return
    
    ratio = length_a / length_b
    print(f"The ratio of {length_a} to {length_b} is {ratio}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used here.
    len1 = 20.5
    len2 = 4
    
    calculate_ratio(len1, len2)