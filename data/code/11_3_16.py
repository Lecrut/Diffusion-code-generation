def calculate_ratio(a: float, b: float) -> float | None:
    """Calculate the ratio of two numbers a/b."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both values must be numeric.")
    
    try:
        return a / b
    except ZeroDivisionError:
        # Cannot divide by zero; handle gracefully.
        pass

def main():
    """Execute the program logic with hard-coded sample values."""
    # Sample values for demonstration without user input
    length_a = 10.5
    length_b = 3
    
    try:
        ratio_value = calculate_ratio(length_a, length_b)
        
        if isinstance(ratio_value, float):
            print(f"The ratio of {length_a} to {length_b} is:")
            print(f"{ratio_value:.2f}")
            
        else:
            # Should not happen given the try/except block above for valid division
            print("An error occurred during calculation.")

    except ZeroDivisionError as e:
        print(f"Graceful handling of zero-division error: {e}")
    
if __name__ == '__main__':
    main()