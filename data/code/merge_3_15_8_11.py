import functools

# Predefined constant value to check against function results
TARGET_VALUE = 42

def match_checker(target: int) -> callable:
    """
    Decorator that checks if the result of a decorated function matches 
    a predefined target integer. Returns None or raises an error on mismatch.
    
    Args:
        target (int): The expected value returned by the wrapped function.
        
    Returns:
        callable: A wrapper function that executes the original logic and validates output.
    """

    def decorator(func) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if result != target:
                raise ValueError(f"Function returned {result}, but expected {target}")
                
            return result
        
        return wrapper

    return decorator

if __name__ == '__main__':
    # Sample function to be decorated
    def add_numbers(a, b):
        """Returns the sum of two numbers."""
        return a + b
    
    @match_checker(target=TARGET_VALUE)
    def test_sum():
        """Test case that should match the target value."""
        return 10 + 32

    # Another sample function with mismatched result (for demonstration if removed, it would raise error)
    # Uncommenting below to see decorator in action: