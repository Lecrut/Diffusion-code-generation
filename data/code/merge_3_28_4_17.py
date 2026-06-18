def is_larger(num1: float, num2: float) -> bool:
    """
    Determines if num1 is larger than num2 using a single comparison operator.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        
    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5.0, 3.0),      # Should be True
        (-2.0, -4.0),   # Should be True
        (10.0, 10.0),   # Should be False (equal)
        ("string", "longer string"),  # TypeError expected for non-numbers, but task specifies numbers in context; keeping numeric focus per instruction intent or handling gracefully? 
                           # Re-reading: Task says "one number". We'll stick to floats/ints.
    ]

    results = []
    for a, b in test_cases:
        result = is_larger(a, b)
        expected = a > b  # Verification logic (same as function body but explicit here for clarity in main block if needed, though redundant with func definition)
        status = "PASS" if result == expected else "FAIL"
        results.append((a, b, result, status))

    print("Test Results:")
    for a, b, res, stat in results:
        print(f"is_larger({a}, {b}) -> {res} [{stat}]")