def is_greater_than(num1: float, num2: float) -> bool:
    """Returns True if num1 > num2 using a built-in comparison operator."""
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    sample_a = 50
    sample_b = 75

    result = is_greater_than(sample_a, sample_b)
    
    # Outputting a simple confirmation string since no output method was specified, 
    # but standard print behavior assumes it's acceptable for runnable modules unless forbidden otherwise.
    print(f"Is {sample_a} larger than {sample_b}? Result: {result}")