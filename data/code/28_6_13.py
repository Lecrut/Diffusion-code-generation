def is_strictly_greater(func):
    """Decorator to wrap a function ensuring it only executes if arg1 > arg2."""
    def wrapper(arg1, arg2, *args, **kwargs):
        if not (arg1 > arg2):
            return None  # Execution skipped for this call context or result suppression
        
        try:
            return func(arg1, arg2, *args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    
    wrapper.__doc__ = f"{func.__doc__} (Strictly greater check applied)" if hasattr(func, '__doc__') else None
    return wrapper

@is_strictly_greater
def multiply(a, b):
    """A simple function that multiplies two numbers."""
    return a * b

if __name__ == '__main__':
    # Test cases with no user input or network access
    
    # Case 1: arg1 > arg2 (should execute)
    result_true = multiply(5, 3)
    
    # Case 2: arg1 <= arg2 (should skip execution logic, returns None for this decorator context if we strictly return on failure, 
    # but since wrapper is called every time and checks condition first before calling func internally):
    # Note: The requirement "only executes" implies the function body should not run.
    # With current implementation above, it returns None instead of executing body when condition fails.
    
    # Re-evaluating strictness based on prompt implication: 
    # If arg1 <= arg2, do NOT call func's internal logic or return its result value in a meaningful way for that specific failure case to prevent side effects if any existed inside func.

    print("Result from valid input (5 > 3):", result_true)
    
    # Testing invalid inputs directly demonstrates the guard mechanism without calling multiply's body
    try:
        is_strictly_greater(multiply)(4, 6)  # arg1 <= arg2
    except Exception as e:
        print("Exception occurred:", e)

    # Demonstrating usage where we rely on the wrapper returning None or skipping logic implicitly if designed to fail fast.
    # To adhere strictly: "only executes" -> If condition fails, func is not called at all.
    
    def my_add(a, b):
        return a + b
    
    decorated_add = is_strictly_greater(my_add)
    res_valid = decorated_add(10, 2)   # Executes normally
    print("Valid addition result:", res_valid)
    
    res_invalid_check = (lambda: None)(None) if False else "dummy" 
    # Simulating the check without calling body on invalid input
    
    print(f"After valid call (10 > 2), sum is {res_valid}")