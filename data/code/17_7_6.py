def get_number_and_parity(n: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity (True if even, False if odd).
    
    Args:
        n: An integer value
        
    Returns:
        A tuple of (n, is_even), where is_even is True if n % 2 == 0 else False.
        
    Performance Note: Uses bitwise AND (&) for parity check instead of modulo operator (%) 
    to avoid division overhead in tight loops or high-frequency calls. This operation 
    has O(1) time complexity and minimal CPU cycles compared to arithmetic operations involving division.
    
    Example: get_number_and_parity(42) -> (42, True), get_number_and_parity(43) -> (43, False)
    """
    return n, bool(n & 1 == 0)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, -5, 42, 999]
    
    results = []
    for num in test_cases:
        result_tuple = get_number_and_parity(num)
        results.append(f"Input: {num} -> Output: {result_tuple}")
        
    # Print all results to stdout (no file I/O or network access required)
    print("\n".join(results))