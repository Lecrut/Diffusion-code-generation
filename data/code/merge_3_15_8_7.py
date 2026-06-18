import functools

# Predefined constant value to check against
EXPECTED_VALUE = 42

def match_checker(expected_value: int) -> callable:
    """
    A decorator that wraps a function and checks if its result matches 
    the predefined expected value. If it does, it returns True; otherwise, False.
    
    Args:
        expected_value (int): The constant value to compare against.

    Returns:
        Callable[[Any], Any]: Wrapper function that executes the original logic 
                             and compares results with EXPECTED_VALUE.
    """
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # Check if the actual result matches the expected constant value
            is_match = (result == EXPECTED_VALUE)
            
            return is_match
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    def add(a: int, b: int) -> int:
        """Simple addition function."""
        return a + b

    # Apply the match_checker decorator with EXPECTED_VALUE (42)
    @match_checker(EXPECTED_VALUE)
    def sum_three(x: int, y: int, z: int) -> int:
        """Function that returns 13 when called with specific inputs."""
        return x + y + z

    # Test the decorated function directly (should return False since 4+5+6=15 != 42)
    result_sum_three = sum_three(4, 5, 6)
    
    print(f"Result of {sum_three.__name__}(4, 5, 6): {result_sum_three}")

    # Test the wrapper function itself (should return True if we define a matching logic below)
    def make_matcher():
        """Helper to create a scenario where result equals EXPECTED_VALUE."""