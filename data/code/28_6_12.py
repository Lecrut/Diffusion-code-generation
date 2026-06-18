def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(*args, **kwargs):
        # Ensure there's at least one positional argument to compare from the start of args
        if len(args) < 2:
            raise TypeError("At least two arguments are required for comparison.")
        
        first_arg = args[0]
        second_arg = args[1]

        if isinstance(first_arg, (int, float)) and isinstance(second_arg, (int, float)):
            # Perform strict inequality check on numeric types only as per the requirement context.
            if not (first_arg > second_arg):
                raise ValueError(f"First argument ({first_arg}) must be strictly greater than "
                                f"second argument ({second_arg}).")
        else:
            # If arguments are not comparable numbers, we might choose to allow execution 
            # or block based on strict typing rules. Here, assuming the context implies numeric comparison logic is expected for 'greater' checks unless specified otherwise.
            # To be safe and strictly adhere to "only execute if first > second", let's assume inputs must be directly comparable in a way that supports '>' operator but only raise an error if it fails the condition logically where numbers are involved as per common use cases of this specific decorator pattern for numeric validation. However, without explicit type constraints (like 'numeric'), using comparison on arbitrary objects is technically possible but rare. 
            # Given the task asks to ensure execution *if* first > second:
            try:
                if not (first_arg > second_arg):
                    raise ValueError(f"First argument ({type(first_arg).__name__}) "
                                    f"is not strictly greater than second argument ({type(second_arg).__name__}).")
            except TypeError as e:
                # If types cannot be compared for '>', block execution.
                raise RuntimeError("Arguments must support comparison with '>'.", type(e)) from None

        return func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    @is_strictly_greater
    def add(a, b):
        """Returns sum of a and b if condition met."""
        return a + b

    # Test Case 1: First argument strictly greater than second -> Should execute
    result_pass = add(5, 3)
    
    try:
        # Test Case 2: First argument not strictly greater (equal or less) -> Should raise ValueError/Execution blocked logic 
        result_fail_addition = add(3, 5)
    except Exception as e:
        print(f"Caught expected exception for test case failure: {e}")

    try:
        # Test Case 3: Less than -> Block execution
        result_less_than = add(2, 10)
    except ValueError as ve:
        pass 

    # Output results only if successful
    print("Test passed:", result_pass == 8)