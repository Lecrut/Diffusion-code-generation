import functools

def check_eq(func):
    """
    Decorator that enforces strict equality checking between any two functions 
    passed to it during the function definition phase (via *args).
    
    This decorator expects the decorated function to accept at least one argument,
    which is a tuple of functions. It then checks if all those functions are strictly equal.
    If they are not equal, an AssertionError is raised immediately upon calling 
    the wrapped function with any arguments.

    Args:
        func (callable): The original function to decorate.

    Returns:
        callable: A wrapper that performs strict equality checking on provided functions.
    
    Raises:
        AssertionError: If two or more passed-in functions are not strictly equal.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the tuple of functions from args (assuming first arg is a tuple of funcs)
        if len(args) < 1:
            raise AssertionError("At least one argument containing functions must be provided.")

        func_tuple = args[0]
        
        # Ensure it's actually iterable and contains callables
        try:
            iter(func_tuple)
        except TypeError:
            raise AssertionError(f"First argument {func_tuple} is not an iterable of functions.")

        if len(func_tuple) < 2:
            raise AssertionError("At least two functions must be passed for comparison.")

        # Perform strict equality check between all pairs in the tuple
        funcs = list(func_tuple)
        n = len(funcs)
        
        for i in range(n):
            for j in range(i + 1, n):
                if not (funcs[i] == funcs[j]):
                    raise AssertionError(
                        f"Strict equality check failed: {func_name} != {func_other_name}"
                    )

        # If checks pass, proceed with normal execution logic placeholder
        return func(*args[1:], **kwargs)

    def get_func_names():
        """Helper to retrieve function names for error messages."""
        try:
            funcs = list(func_tuple) if 'func_tuple' in locals() else []
            return [f.__name__ for f in funcs]
        except NameError:
            return ["Unknown Function"]

    # Bind helper logic dynamically or via closure adjustment if needed, 
    # but since we can't access inner scope easily without re-structuring slightly here.
    # We'll adjust the wrapper to capture args at runtime properly for error messages.
    
    @functools.wraps(wrapper)
    def final_wrapper(*args, **kwargs):
        func_tuple = args[0] if len(args) > 1 else None
        
        try:
            funcs_list = list(func_tuple)
            
            # Check equality strictly between all pairs
            for i in range(len(funcs_list)):
                for j in range(i + 1, len(funcs_list)):
                    f_i = funcs_list[i]
                    f_j = funcs_list[j]
                    
                    if not (f_i == f_j):
                        raise AssertionError(
                            f"Strict equality check failed between functions: "
                            f"{getattr(f_i, '__name__', 'unknown')} != {getattr(f_j, '__name__', 'unknown')}"
                        )
        except TypeError as e:
            if "not iterable" in str(e):
                raise AssertionError("First argument must be an iterable of functions.") from None
            
        # If all checks passed, call the original function with remaining args/kwargs
        return func(*args[1:], **kwargs)

    final_wrapper.__doc__ = f"{func.__doc__} (Enforces strict equality between provided functions)"
    
    return final_wrapper

if __name__ == '__main__':
    # Sample usage demonstrating the decorator functionality
    
    def add(a, b):
        """Adds two numbers."""
        return a + b

    def multiply(x, y):
        """Multiplies two numbers."""
        return x * y

    @check_eq
    def verify_operations(funcs_tuple):
        """Verifies that all provided functions are strictly equal."""
        print("Functions verified as strictly equal.")
    
    # Test Case 1: All same function (should pass)
    try:
        result = verify_operations((add, add))
        print(f"Test 1 Result: {result}")
    except AssertionError as e:
        print(f"Test 1 Failed: {e}")

    # Test Case 2: Different functions (should fail immediately on call)
    try:
        result = verify_operations((add, multiply))
        print("This line should not be reached.")
    except AssertionError as e:
        print(f"Test 2 Correctly Caught Error: {e}")

    # Test Case 3: Three same functions (should pass)
    try:
        result = verify_operations((multiply, add, multiply))
        print("Functions verified as strictly equal.")
    except AssertionError as e:
        print(f"Test 3 Failed: {e}")