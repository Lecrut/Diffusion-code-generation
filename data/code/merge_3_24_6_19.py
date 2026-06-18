class NegativeResultError(Exception):
    """Custom exception raised when a function returns a negative result."""
    pass

def check_non_negative(func):
    """Decorator that checks if the decorated function's result is non-negative.
    
    If the result is less than zero, raises a NegativeResultError with details about 
    the failed call and its return value. Otherwise, it proceeds normally.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)) and result < 0:
                raise NegativeResultError(f"Function {func.__name__} returned a negative value: {result}")
            return result
        except Exception as e:
            # Re-raise any original exceptions without hiding them
            raise

    return wrapper

def calculate_distance(x1, y1, x2, y2):
    """Calculates the Euclidean distance between two points. 
    Returns a negative value if an error condition is artificially simulated."""

if __name__ == '__main__':
    pass
