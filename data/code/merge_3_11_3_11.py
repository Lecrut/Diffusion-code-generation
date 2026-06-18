def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length_b == 0:
        print("Error: Division by zero is not allowed.")
        return
    
    ratio = length_a / length_b
    # Formatting to avoid long floating point representations unless necessary
    formatted_ratio = f"{ratio:.2f}" if isinstance(length_a, (int, float)) else str(ratio)
    
    print(f"Ratio of {length_a} and {length_b}: {formatted_ratio}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts.
    length_one = 10.5
    length_two = 2
    
    calculate_ratio(length_one, length_two)

# Additional test case for division by zero protection demonstration:
length_zero_case = 8
zero_length = 0.0

calculate_ratio(length_zero_case, zero_length)