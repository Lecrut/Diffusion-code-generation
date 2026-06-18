def calculate_ratio(length_a: float, length_b: float) -> None:
    """Calculates and prints the ratio of two lengths."""
    try:
        if length_b == 0:
            print("Error: Division by zero is not allowed.")
            return
        
        ratio = length_a / length_b
        print(f"The ratio of {length_a} to {length_b} is {ratio}.")
    
    except ZeroDivisionError as e:
        print(f"An error occurred during calculation: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    length_one = 10.5
    length_two = 2
    
    calculate_ratio(length_one, length_two)

# Additional test case with zero denominator to demonstrate error handling
calculate_ratio(5, 0)