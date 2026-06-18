def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(*args, **kwargs):
        # Extract arguments to check condition (first two positional args)
        if len(args) < 2:
            raise TypeError("is_strictly_greater requires at least two positional arguments")
        
        a = args[0]
        b = args[1]

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            # Handle non-numeric types by attempting comparison without raising early errors on type mismatch logic beyond basic check
            try:
                result = a > b
            except TypeError:
                raise ValueError(f"Arguments must be numeric. Got {type(a).__name__} and {type(b).__name__}")

        if not result:
            return None  # Signal that execution was skipped due to condition failure
        
        return func(*args, **kwargs)
    
    wrapper.__name__ = f"{func.__name__}_strict"
    return wrapper

if __name__ == '__main__':
    def add(a, b):
        """Simple function to test the decorator."""
        print(f"Adding {a} + {b}")
        return a + b

    # Test case 1: First argument strictly greater than second (should execute)
    result = is_strictly_greater(add)(5, 3)
    
    # Test case 2: First argument not strictly greater than second (should NOT execute function body)
    result_skip = is_strictly_greater(add)(4, 6)

    print(f"Result of add(5, 3): {result}")
    if result_skip is None:
        print("add(4, 6) was skipped as expected.")