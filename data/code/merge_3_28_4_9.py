def is_greater(a: float, b: float) -> bool:
    """
    Determines if 'a' is strictly greater than 'b'.
    
    Uses Python's built-in comparison operator '>' which is implemented in C,
    ensuring it is as fast and efficient as possible. No additional arithmetic
    or function calls are performed beyond the single comparison operation.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        (10.5, 3),          # Expected: True
        (-2.7, -4.9),       # Expected: True
        (0, 0),             # Expected: False
        ("apple", "banana"),# Note: Comparing strings with > also works in Python for lexicographic order, but the prompt implies numbers. 
                           # However, to strictly adhere to 'number' context while keeping code runnable and general, we stick to numeric types as primary logic.
                           # If extended to mixed types or generic objects, standard comparison still applies. 
                           # For this specific task focusing on numbers:
        (1e-5, 0)           # Expected: True
    ]

    print("Running optimization test for number comparison...")
    
    passed_count = 0
    total_tests = len(samples)

    for i in range(total_tests):
        val_a, val_b = samples[i]
        
        if isinstance(val_a, str) or isinstance(val_b, str):
            # Skip string comparisons to ensure we strictly test numeric optimization as requested.
            continue
            
        expected_result = is_greater(val_a, val_b)

    print(f"Test suite completed for {total_tests - sum(1 for v in samples if not all(isinstance(x, (int, float)) and isinstance(v[0], str)))} numeric cases.")