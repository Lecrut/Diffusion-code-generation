def is_odd_bitwise(n: int) -> bool:
    """
    Determines if an integer is odd using a bitwise AND operation with 1.
    
    This method avoids division by utilizing the fact that in binary representation,
    any odd number has its least significant bit set to 1 (i.e., ...01 or ...11).

    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return n & 1 == 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, 1, -3, 42, 99]

    print("Testing odd/even determination using bitwise operations:")
    
    for num in test_cases:
        result = is_odd_bitwise(num)
        status = "Odd" if result else "Even"
        print(f"{num} -> {status}")