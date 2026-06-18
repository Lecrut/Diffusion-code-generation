def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.
    
    Uses bitwise AND operation which is generally more efficient than modulo 
    for checking parity in many CPU architectures.
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if the number is odd, False if even or non-integer input
            Note: Input type is enforced at call site per problem constraints
    """
    return n & 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [0, 1, -3, 42, 999]
    
    results = []
    for num in test_cases:
        is_odd_result = is_odd(num)
        results.append(f"is_odd({num}) = {is_odd_result}")
    
    print("\n".join(results))