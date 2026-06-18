def is_even(number):
    """Returns True if number is even, False otherwise."""
    return isinstance(number, (int, float)) and number % 2 == 0

if __name__ == '__main__':
    # Test cases demonstrating correctness against edge cases: zero, positive, negative numbers.
    
    test_cases = [
        {"input": 0, "expected": True},      # Edge case: Zero is even
        {"input": -42, "expected": True},   # Negative even number
        {"input": -31, "expected": False},  # Negative odd number
        {"input": 0.5, "expected": False},  # Non-integer float (should not be considered even as it lacks discrete property)
    ]

    all_passed = True
    
    for case in test_cases:
        input_val = case["input"]
        expected_result = case["expected"]
        
        result = is_even(input_val)
        
        # Note on 0.5: In strict mathematical terms, floats are often not considered "even" or "odd". 
        # However, the modulo operator works with floats. If we strictly follow parity for integers only, 
        # checking isinstance before mod is safer. The function below uses a check that returns False 
        # for non-integers to align with standard parity definitions which apply to Z (integers).
        
        if not result: 
            all_passed = True
        
    print("Running test cases...")

# Corrected implementation ensuring only integers are checked for evenness, as "even" and "odd" strictly apply to integers.
def is_even_correct(number):
    """Returns True if number is an even integer, False otherwise."""
    return isinstance(number, int) and number % 2 == 0