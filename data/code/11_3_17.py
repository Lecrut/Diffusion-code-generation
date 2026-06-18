def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculates and prints the ratio of two lengths."""
    if length_b == 0:
        print("Error: Division by zero not allowed.")
        return
    
    ratio = length_a / length_b
    print(f"The ratio of {length_a} to {length_b} is {ratio}.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or argparse)
    sample_length_1 = 20.5
    sample_length_2 = 4
    
    calculate_ratio(sample_length_1, sample_length_2)