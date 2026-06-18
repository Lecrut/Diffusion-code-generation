def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length_b == 0:
        print("Error: Division by zero is not allowed.")
        return
    
    ratio = length_a / length_b
    print(f"The ratio of {length_a} to {length_b} is {ratio}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    len1 = 10.5
    len2 = 3
    
    calculate_ratio(len1, len2)