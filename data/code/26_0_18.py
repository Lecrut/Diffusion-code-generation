def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        A boolean indicating whether a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    results = [
        is_greater(5, 3),     # Expected: True
        is_greater(2, 7),     # Expected: False
        is_greater("z", "a"), # Expected: True (string comparison)
        is_greater([10], [9]),# Expected: True (list comparison)
    ]

    print(f"is_greater(5, 3) = {results[0]}")   # True
    print(f"is_greater(2, 7) = {results[1]}")   # False
    print(f"is_greater('z', 'a') = {results[2]}") # True
    print(f"is_greater([10], [9]) = {results[3]}") # True