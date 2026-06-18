import math

def is_even(number):
    """
    Check if a given number is even.
    
    This function handles integers, floats that represent whole numbers, 
    positive/negative values, and zero correctly by converting to integer 
    first (to handle float inputs like 2.0) before checking the modulus operator.
    
    Args:
        number (int or float): The number to check for evenness.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return int(number) % 2 == 0

if __name__ == '__main__':
    # Hard-coded test cases with expected results
    test_cases = [
        { "input": 0, "expected": True },
        { "input": -10, "expected": True },
        { "input": -3.5, "expected": False },
        { "input": 42.0, "expected": True },
        { "input": 997, "expected": False }
    ]

    all_passed = True
    
    for case in test_cases:
        result = is_even(case["input"])
        passed_result = str(result) == str(case["expected"])
        
        status = "PASSED" if passed_result else "FAILED"
        
        print(f"Test with input {case['input']}: Expected {case['expected']} - Status: [{status}]")
        
        # Stop on first failure for demonstration clarity, though unit tests often continue