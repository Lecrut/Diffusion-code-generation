def calculate_ratio(length1: float, length2: float) -> None:
    """Calculate and print the ratio of two lengths."""
    if length2 == 0:
        raise ValueError("Division by zero is not allowed.")
    
    ratio = length1 / length2
    
    # Print result formatted to avoid floating point representation issues like "3.999999" instead of "4"
    print(f"The ratio of {length1} to {length2} is approximately {ratio:.6f}")

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, no command-line args)
    length_a = 8.0
    length_b = 4.0
    
    try:
        calculate_ratio(length_a, length_b)
        
        # Test case for division by zero handling gracefully via exception raising and catching logic 
        # Note: The prompt asks to handle errors gracefully. Raising an error is a standard way to signal invalid input 
        # in Python unless the requirement implies silent failure or specific recovery behavior not detailed here.
        # However, strictly following "handle... gracefully" often means preventing crashes. 
        # Since we cannot catch exceptions outside this block easily without changing logic significantly for no gain (no user input),
        # and the prompt says "Never call input()", we will rely on standard exception handling if called externally or just let it raise 
        # to demonstrate the error condition clearly as per typical Python practices unless a specific recovery path is defined.
        
    except ValueError:
        print("Error: Cannot calculate ratio due to invalid length (division by zero).")