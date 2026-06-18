import math

def is_positive(value: float) -> bool:
    """
    Check if a given float value is positive.
    
    This function uses standard comparison operators which handle 
    floating-point precision adequately for typical use cases where 
    exact zero or strictly greater than zero checks are required without 
    custom epsilon thresholds specified in the task description.
    
    Args:
        value (float): The number to check
        
    Returns:
        bool: True if value is positive, False otherwise
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    test_values = [1.5, -3.2, 0.0, 4e-8, float('-inf'), float('inf')]
    
    print("Testing is_positive function:")
    for val in test_values:
        result = is_positive(val)
        status = "Positive" if result else "Not Positive (Zero or Negative)"
        print(f"{val}: {status}")