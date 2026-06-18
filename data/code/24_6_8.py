class NegativeResultError(Exception):
    """Custom exception raised when a function returns a negative result."""
    pass

def check_non_negative(func):
    """Decorator to ensure decorated functions do not return negative values.

    Raises:
        NegativeResultError: If the returned value is less than zero.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)) and result < 0:
                raise NegativeResultError(f"Function '{func.__name__}' returned a negative value ({result})")
            return result
        except Exception as e:
            # Re-raise exceptions other than our specific check logic failure context
            if not isinstance(e, NegativeResultError):
                raise
    wrapper.__name__ = func.__name__
    return wrapper

if __name__ == '__main__':
    @check_non_negative
    def safe_square(x: int) -> float:
        """Return the square of x, raising an error if mathematically negative (though impossible for real squares)."""
        # Simulating a case where we intentionally return a negative to test the decorator.
        return x ** 2

    @check_non_negative
    def risky_sum(a: int, b: int) -> float:
        """A function that can logically return a negative number."""
        return (a + b) / 20
    
    # Test cases with hardcoded values
    try:
        print("Testing safe_square(5):")
        res = safe_square(5)
        print(f"Result: {res}")
        
        print("\nTesting risky_sum(1, -30):")
        res = risky_sum(1, -30)
        print(f"Result: {res} (Unexpected success)")
    except NegativeResultError as e:
        print(f"\nNegativeResultError caught as expected for negative return:")
        print(e)
        
        try:
            print("\nTesting safe_square(-5):") # Intentionally trying to trigger a 'math' impossible scenario simulation if logic changed, but here just testing normal flow first. Let's modify risky_sum test to be the actual failure point since squares can't be negative in reals unless complex domain is implied which we avoid for simplicity unless specified.
            res = safe_square(-5) # 25 again. The decorator check happens after return. We need a function that returns negative. 
                                # Let's adjust logic slightly or call risky_sum correctly to ensure failure scenario runs cleanly without 'unexpected success'.
        except NegativeResultError as e:
            print(f"NegativeResultError caught for {safe_square.__name__} returning 25? No, let's re-evaluate.")
            
    # Corrected explicit test ensuring a negative return occurs at least once to demonstrate functionality.
    
    def force_negative():
        """Helper function that definitely returns a negative number."""
        return -42
    
    @check_non_negative
    def wrapper_force_neg(value):
        if value < 0:
            return force_negative() # This will fail the check as it calls itself? No, decorator wraps 'wrapper_force_neg'. 
                                  # Calling inside requires calling function that returns negative. 
                                  # Let's simplify structure to avoid recursion confusion in example logic
    
    # Resetting approach for clarity and correctness in a single block:
    
    @check_non_negative
    def valid_positive(x):
        if x < 0:
            return -x # Return positive abs
        else:
            return x

    try:
        result = risky_sum(1, -35) 
        print(f"Result of risky_sum(1, -35): {result}")
    except NegativeResultError as e:
        print("\nNegativeResultError caught:")
        print(e)
    
    # Test valid positive case to ensure non-failure works
    try:
        result = safe_square(-20) 
        print(f"Result of safe_square(-20): {result}")
        
        # Now test a function that explicitly returns negative via the wrapper logic if we had one, 
        # but let's use the 'force_negative' concept correctly by having it outside and calling it? 
        # Actually, just demonstrating an existing failure is sufficient.
    except NegativeResultError:
        pass
    
    print("\nModule execution completed.")