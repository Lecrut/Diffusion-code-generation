def is_odd_bitwise(n: int) -> bool:
    """
    Determines if an integer is odd using bitwise operations.
    
    An integer n in binary representation has its least significant bit (LSB) set 
    to 1 if it is odd, and 0 if it is even. The expression 'n & 1' performs a bitwise AND 
    between the number and 1. If the result is truthy (non-zero), the number is odd; otherwise, it is even.
    
    This approach avoids division/modulo operations which are computationally more expensive than bit shifts/ANDs.

    :param n: The integer to check.
    :return: True if n is odd, False otherwise.
    """
    return (n & 1) != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    test_cases = [3, -5, 42, -7]

    print("Testing odd/even detection using bitwise AND:")
    for num in test_cases:
        result = is_odd_bitwise(num)
        status = "Odd" if result else "Even"
        binary_repr = f"{num:b}"[:30].ljust(32, ' ')  # Pad with spaces to align bits visually up to sign bit range roughly
        print(f"Number: {num} (Binary approx: ...{binary_repr[-4:]}) -> Status: {status}")