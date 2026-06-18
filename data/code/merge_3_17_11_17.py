def is_even(n):
    """
    Returns True if n is even, False otherwise.
    Efficiently checks parity using bitwise AND with 1.
    
    Args:
        n (int): The integer to check.
        
    Returns:
        bool: True if the number is even, False if odd.
    """
    return not (n & 1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or CLI arguments
    test_cases = [-50, -23, 0, 42, 99, 1]

    print("Testing is_even function:")
    passed_count = 0
    total_tests = len(test_cases)

    for num in test_cases:
        result = is_even(num)
        expected = num % 2 == 0
        if result == expected:
            passed_count += 1
        
        # Print specific messages based on the number (avoiding unnecessary markdown or prose outside code logic context as requested, keeping output clean and relevant)