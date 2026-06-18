def read_float(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError as e:
        raise TypeError(f"Non-numeric input received: '{value}'. Error details: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    weight1_str = "75.5"
    weight2_str = "68.0"

    try:
        weight1 = read_float(weight1_str)
        weight2 = read_float(weight2_str)
        
        difference = weight1 - weight2
        
        # Print the result formatted to two decimal places for clarity
        print(f"{difference:.2f}")
    
    except TypeError as e:
        # Handle non-numeric input errors gracefully
        print("Error:", str(e))