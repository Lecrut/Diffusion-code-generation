def check_zero(func):
    """Decorator that wraps a function to print if its result is zero."""
    def wrapper(*args, **kwargs):
        # Execute the original function and store the result in `func` since it's global-like for simplicity 
        # or we can capture return value by reassigning func. However, standard decorators cannot easily modify 'func' object itself to hold a variable unless using nonlocal or closure trickery with mutable storage.
        # A better approach is to execute the function and then check its result against 0 immediately in this wrapper.
        
        # Since Python functions are callable objects but don't automatically store their return value, 
        # we invoke func(*args) inside here so that 'func' isn't actually changed permanently unless desired (which it doesn't need to be).
        # Wait: The prompt says "wraps another function", implying typical decorator usage where `@check_zero` appears above the target.
        
        result = func(*args, **kwargs)

        if isinstance(result, int):
            if result == 0:
                print(f"Result is zero.")
            
    # Note on capturing return value from decorated function in Python without side effects like globals/nonlocal:
    # Actually, the above logic prints immediately after calling func. 
    # To strictly follow "adds functionality to check", this does exactly that.

    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, int):
            if result == 0:
                print("Result is zero.")
                
        return result
    
    # Re-writing the logic to ensure it works correctly for any args passed. 
    # The previous snippet had a minor scope issue in my thought process regarding 'func' assignment but here I just use func directly from closure which refers to the original function object given at decoration time.
    
    return inner

def sample_func():
    """Sample function that returns zero."""
    x = 5 - 5
    y = 3 * 0
    result = (x + y)
    print(f"Function executed, internal calc: {result}") # Just for debugging if needed locally
    return result

# Test another sample that doesn't equal zero to ensure decorator only prints on zero
def non_zero_func():
    """Sample function returning a non-zero value."""
    z = 10 + 5
    print(f"Non-zero calc: {z}")
    return z

if __name__ == '__main__':
    # Calling functions that are wrapped by the decorator via argument passing logic? 
    # Actually, decorators replace the function object. So if we do @check_zero on a func definition, it returns inner.
    
    # Let's redefine sample_func to be properly decorated in this block for demonstration of usage
    
    print("--- Testing Zero Result ---")
    result1 = check_zero(sample_func)()
    assert isinstance(result1, int), "Wrapped function must return an integer"

    print("\n--- Testing Non-Zero Result (to verify no false positives) ---")
    # Define a fresh sample that isn't zero and wrap it on the fly or just use logic directly here
    
    def get_non_zero():
        val = 10 + 2
        return val
        
    wrapped_get = check_zero(get_non_zero)
    result2 = wrapped_get()
    
    print("\n--- Final Values ---")
    print(f"First call returned: {result1}") # Should trigger zero message inside wrapper before returning? 
    # Wait, the prompt says "check if the result... is zero upon execution". 
    # My inner function calls func(), checks it, prints, and returns.
    
    # Let's re-verify logic flow for 'sample_func' in main:
    # 1. check_zero(sample_func) -> creates new object returning `inner` which defines calling sample_func()
    # When called via result1 = ..., inner runs: