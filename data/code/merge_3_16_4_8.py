def check_all_positive(numbers):
    """
    Check if all numbers in a list are positive (greater than zero).
    
    Args:
        numbers (list of float/int): List of numerical values to check.
        
    Returns:
        bool: True if all numbers are strictly greater than 0, False otherwise.
        Uses early termination for optimization; returns immediately upon finding a non-positive number.
    """
    return not any(num <= 0 for num in numbers)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ([1, 2, 3], True),           # All positive -> True
        ([-1, -2, 3], False),       # Contains negative -> False
        ([0, 5, 10], False),        # Contains zero -> False
        ([], True),                 # Empty list is treated as all conditions met (vacuously true) logic applied via 'any' returning False for non-positive check? 
                                    # Correction: any() returns False if no positive numbers found <= 0 exists in the generator expression's negation context.
                                    # Let's trace logic carefully:
                                    # Case [] -> not any(x <= 0 for x in []) -> not False -> True. Correct.
        ([1, -2], False),           # Mixed signs -> False
    ]

    results = []
    test_list_name = [name] if isinstance(name, list) else f"len_{len(numbers)}"
    
    print("Running positive number checks...")
    for i, (test_data, expected) in enumerate(sample_cases):
        result = check_all_positive(test_data)
        passed = "PASS" if result == expected else "FAIL"
        
        # Format output clearly showing input and boolean result
        formatted_input = str(list(test_data)) + f"(len={len(test_data)})"
        results.append((test_list_name, result, passed))

    for item in results:
        print(f"{item[0]} | Input: {formatted_input} => Result: {bool(item[1])} [{(2 if item[1] == True else 3)}]")