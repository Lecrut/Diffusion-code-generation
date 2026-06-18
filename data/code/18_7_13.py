def compare_large_integers(a: int, b: int) -> bool:
    """
    Compares two potentially large integers without explicit overflow concerns.
    
    Python's native integer support handles arbitrarily large numbers automatically,
    so direct comparison is both safe and efficient for this task.
    
    Args:
        a (int): The first integer to compare.
        b (int): The second integer to compare.
        
    Returns:
        bool: True if a equals b, False otherwise.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing large integer comparison
    # Using numbers that exceed standard 64-bit limits to demonstrate capability
    
    value_a = 2 ** 100 + (3 ** 80) * 7
    value_b = 2 ** 95 + (3 ** 80) + 100
    
    result_a_gt_b = compare_large_integers(value_a, value_b - 1)
    result_equal = compare_large_integers(42, 42)
    
    print(f"Comparison of large integers: {value_a} and {value_b}")
    # Note: We test if a equals b-1 to show inequality logic works as well
    
    # Additional explicit comparison for clarity in the output context
    is_equal = value_a == value_b
    print(f"Are they equal? {is_equal}")
    
    # Demonstrate that direct comparison handles large values correctly
    sample_large_1 = 10 ** 50 + 9 ** 48
    sample_large_2 = 9 ** 48
    
    is_sample_greater_than = sample_large_1 > sample_large_2
    print(f"Is {sample_large_1} greater than {sample_large_2}? {is_sample_greater_than}")