import sys

def is_strictly_greater(a: float | int, b: float | int) -> bool:
    """
    Check if number 'a' is strictly greater than number 'b'.
    
    Parameters are validated to ensure they are numeric. Non-numeric inputs 
    will raise a TypeError with an informative message.
    
    Args:
        a (float|int): The first number to compare.
        b (float|int): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an integer or float.
    """
    try:
        # Explicit type checking for robustness against subclasses of int/float 
        # that might behave unexpectedly in comparisons (though Python's duck typing usually handles this).
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Both arguments must be numeric. Received: {type(a).__name__} and {type(b).__name__}")
        
        # Ensure we are comparing actual numbers, avoiding special cases like NaN if possible 
        # though strictly greater comparison with floats is standard behavior in Python for the task scope.
        return a > b
        
    except Exception as e:
        raise TypeError(f"Invalid input types or values during comparison check.") from e

if __name__ == '__main__':
    pass
