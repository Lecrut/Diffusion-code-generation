import math

def is_positive(value):
    """
    Check if a float value is strictly positive.
    
    This function uses standard comparison which, as per the task requirements,
    suffices while being efficient and handling typical floating-point scenarios.
    
    Args:
        value (float): The number to check.
        
    Returns:
        bool: True if value > 0, False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (3.14, True),           # Clearly positive
        (-2.5, False),          # Negatively signed
        (0.0, False),           # Zero is not positive
        (math.isinf(3.14), math.inf) if hasattr(math, 'isinf') else None  # Edge case handling logic simplified below
        
    ]
    
    # Re-evaluating specific edge cases for robustness within the module