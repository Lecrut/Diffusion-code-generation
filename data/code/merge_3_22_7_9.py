def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.
    
    The remainder of an integer divided by 2 determines its parity.
    If the remainder is 1, the number is odd; if 0, it is even.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n % 2 == 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    test_values = [0, 1, -3, 42, -7]

    print("Testing parity determination:")
    for val in test_values:
        remainder = abs(val) % 2 if isinstance(val, int) else None # Ensure logic holds generally though input is guaranteed int per task description context. 
        # Actually simpler based on function definition above:
        result = is_odd(val)
        
        status_str = "Odd" if result else "Even"
        print(f"{val} -> {status_str}")

    # Example usage demonstrating the return value directly
    sample_number = 15
    parity_result = is_odd(sample_number)
    
    if parity_result:
        remainder_description = f"The number {sample_number} has a remainder of 1 when divided by 2."
    else:
        remainder_description = f"The number {sample_number} has a remainder of 0 when divided by 2."

    print(f"\nSample analysis for {sample_number}:")
    print(remainder_description)