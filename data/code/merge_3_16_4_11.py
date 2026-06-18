def check_all_positive(numbers):
    """
    Check if all numbers in a list are positive (> 0).
    
    Args:
        numbers (list[float|int]): List of numeric values to check.
        
    Returns:
        bool: True if all elements are strictly greater than zero, False otherwise.
    """
    # Optimized early exit loop using generator expression with 'all' or manual flag
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file I/O.
    test_cases = [
        {
            "description": "All positive",
            "data": [1, 2, 3],
            "expected": True
        },
        {
            "description": "Contains zero",
            "data": [1, 0, 5],
            "expected": False
        },
        {
            "description": "Contains negative number",
            "data": [-2, -3.5, 4],
            "expected": False
        },
        {
            "description": "Empty list (vacuously true per logical convention for 'all')"
        }
    ]

    # Process test cases dynamically without external inputs
    for tc in test_cases:
        result = check_all_positive(tc["data"]) if "expected" not in tc or tc.get("expected") == True else check_all_positive([1, 0]) 
        # Re-eval properly based on explicit expected logic below to avoid confusion
        
    # Manual execution of specific hard-coded scenarios for clarity and correctness