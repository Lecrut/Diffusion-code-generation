def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified integer ratio of two lengths (l1 : l2).
    
    Args:
        l1 (int): The first length. Must be non-negative.
        l2 (int): The second length. Must be non-negative and not both zero.
        
    Returns:
        tuple[int, int]: A tuple (a, b) representing the simplified ratio a : b.
                         If inputs are 0, returns (-1, -1).
    
    Raises:
        ValueError: If either input is negative or if both are zero.
    """
    # Handle invalid cases based on problem constraints regarding division by zero and negatives
    if l1 < 0 or l2 < 0:
        raise ValueError("Lengths must be non-negative.")
    
    if l1 == 0 and l2 == 0:
        return -1, -1
    
    # Euclidean algorithm to find GCD
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(l1, l2)
    
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor
    
    return simplified_l1, simplified_l2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    test_cases = [
        (60, 45),   # Expected: 4 : 3
        (8, 12),    # Expected: 2 : 3
        (7, 9),     # Expected: 7 : 9 (coprime)
        (0, 5),     # Edge case with zero length
        (5, 0),     # Edge case with zero length
    ]
    
    print("Testing find_ratio_of_lengths:")
    for l1_val, l2_val in test_cases:
        try:
            result = find_ratio_of_lengths(l1_val, l2_val)
            
            if result == (-1, -1):
                status = "Special case (both zero)"
            else:
                status = f"Ratio {l1_val}:{l2_val} -> {result[0]}:{result[1]}"
                
            print(f"{status}")
        except ValueError as e:
            print(f"Input ({l1_val}, {l2_val}) raised error: {e}")