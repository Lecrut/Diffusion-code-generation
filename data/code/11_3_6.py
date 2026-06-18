import sys

def calculate_ratio(length1: float, length2: float) -> None:
    """Calculates the ratio of two lengths."""
    if length2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    
    ratio = length1 / length2
    print(f"The ratio of {length1} to {length2} is {ratio}.")

if __name__ == '__main__':
    # Sample values for demonstration, avoiding user input and network access.
    sample_length_1 = 10.5
    sample_length_2 = 3
    
    calculate_ratio(sample_length_1, sample_length_2)
    
    # Additional test case with zero divisor to demonstrate error handling gracefully.
    print("\n--- Testing Division by Zero ---")
    calculate_ratio(5, 0)