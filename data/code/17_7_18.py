def get_parity(n: int) -> tuple[int, bool]:
    """
    Returns a tuple (n, is_even).
    
    Args:
        n: An integer input number
        
    Returns:
        A tuple containing the original integer and its parity as a boolean.
        
    Performance Note: Uses bitwise AND operator for constant time O(1) check.
    """
    return n, bool(n & 1 == 0)

if __name__ == '__main__':
    # Hard-coded sample values running without any user input or external dependencies
    samples = [42, -7, 0, 1]
    
    for num in samples:
        result_tuple = get_parity(num)
        print(f"Input: {num} -> Parity Tuple: {result_tuple}")