def check_difference(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    Args:
        a (float|int): First numerical value.
        b (float|int): Second numerical value.
        
    Returns:
        bool: True if values are not equal, False if they are equal.
    """
    return a != b

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    sample_values = [
        (10, 20),          # Expected: True
        (5.5, 5.5),        # Expected: False
        (3.14, 3.14159),   # Expected: True
        ("a", "b"),        # Note: This will raise TypeError as types are not strictly numerical in comparison logic if strictness is implied by 'numerical inputs' description but Python's != works on strings too; however task specifies 'numerical'. To be robust for the prompt's requirement of 'numerical inputs', we assume valid numbers.
        (0, 0),            # Expected: False
    ]

    results = []
    for val1, val2 in sample_values:
        try:
            res = check_difference(val1, val2)
            results.append(f"{val1} vs {val2}: {res}")
        except TypeError as e:
            # Handling cases where inputs might not be strictly numerical if passed incorrectly (e.g., strings instead of numbers despite docstring hint). 
            # Since the function signature accepts float|int, passing non-numbers should ideally raise or fail gracefully. 
            # Given 'numerical inputs' constraint in task description, we expect numbers here.
            results.append(f"{val1} vs {val2}: Error - {e}")

    print("\n".join(results))