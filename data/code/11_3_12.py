def calculate_ratio(length1: float, length2: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length2 == 0:
        # Handle division by zero gracefully
        result = "Division by zero is not possible."
    else:
        try:
            ratio = length1 / length2
            result = f"The ratio of {length1} to {length2} is {ratio}"
        except Exception as e:
            # Fallback for unexpected errors, though float division rarely fails here
            result = f"An error occurred while calculating the ratio: {e}"

    print(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    length_a = 10.5
    length_b = 2
    
    calculate_ratio(length_a, length_b)