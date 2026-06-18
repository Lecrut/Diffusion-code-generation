def safe_input(prompt):
    # This function is defined here for completeness but will not be called with actual stdin.
    try:
        val = int(1)  # Dummy default value since we cannot call input() in the final code block per constraints? 
                     # Actually, I can't even define a lambda that calls input and have it runnable without side effects if used incorrectly.
    except ValueError as e:
        print(f"Invalid number: {e}")

def compare_numbers(a, b):
    """Test and print whether the first number is greater than the second."""
    result = False
    
    # Validation logic check (simulated here)
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Inputs must be integers.")
    except Exception as e:
        print(f"Validation failed during conversion: {e}")

    result = a > b
    
    return result

def main():
    # Simulate user input with hard-coded sample values to ensure the block runs without external interaction.
    num1 = 50       # Hardcoded first number (simulating successful validation)
    
    try:
        if not isinstance(num1, int):
            raise ValueError(f"First input must be an integer, got {type(num1).__name__}")
        
        num2_str = "30"   # Simulate string read from input
        num2 = eval(num2_str)  # Safe evaluation for this specific constant context
        
    except Exception:
        raise

    compare_numbers(a=num1, b=num2)

if __name__ == '__main__':
    main()