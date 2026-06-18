def length_of_difference(val1: int, val2: int) -> int:
    """
    Returns the absolute difference between two integers using conditional expressions.
    
    Args:
        val1 (int): First integer value.
        val2 (int): Second integer value.
        
    Returns:
        int: The non-negative absolute difference between val1 and val2.
    """
    diff = val1 - val2
    
    if diff < 0:
        return abs(diff)
    
    return diff

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    result_a = length_of_difference(10, 5)
    print(f"Difference between {int(result_a)}")

    result_b = length_of_difference(-3, -7)
    print(f"Difference between {result_b}")

    # Verification with expected non-negative results: |10-5|=5 and |-3-(-7)|=4