def calculate_ratio(length1: float, length2: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    
    ratio = length1 / length2
    print(f"The ratio of {length1} to {length2} is {ratio}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used here.
    len_a = 10.5
    len_b = 3
    
    calculate_ratio(len_a, len_b)