def is_strictly_greater(a: float, b: float) -> bool:
    """Check if number a is strictly greater than number b.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare against.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an instance of float or int.
    """
    # Validate input types strictly as per requirement for robustness without external deps
    acceptable_types = (int, float)
    
    def validate_number(value):
        if isinstance(value, acceptable_types):
            return True
        else:
            raise TypeError(f"Expected a number or int/float, got {type(value).__name__}")

    # Validate inputs before comparison to handle errors gracefully with clear messages
    try:
        validate_number(a)
        validate_number(b)
        
        if not (a > b):
            return False
            
    except TypeError as e:
        raise ValueError(f"Invalid input type provided for comparison. {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction or external dependencies
    
    test_cases = [
        (10, 5),      # Expected True
        (3.14, 2.71),# Expected True
        (5, 5),       # Expected False (strictly greater)
        (-1, -5),     # Expected True
        ("string", 5),# Should raise TypeError during validation
        
    ]

    for i in range(len(test_cases)):
        a = test_cases[i][0]
        b = test_cases[i][1]
        
        try:
            result = is_strictly_greater(a, b)
            print(f"Test Case {i+1}: Comparing {a} > {b}")
            print(f"Result: {result}\n")
            
        except (TypeError, ValueError) as e:
            print(f"Test Case {i+1}: Error occurred while comparing {type(a).__name__} and {type(b).__name__}")
            print(f"Exception Message: {e}\n")