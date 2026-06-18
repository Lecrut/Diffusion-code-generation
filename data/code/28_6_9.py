def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(*args, **kwargs):
        # Check condition: first argument must be strictly greater than the second
        if len(args) < 2:
            raise TypeError("is_strictly_greater requires at least two positional arguments")
        
        a = args[0]
        b = args[1]

        try:
            comparison_result = a > b
        except TypeError as e:
            # Handle cases where types cannot be compared (e.g., int vs string)
            print(f"Comparison error between {a} and {b}: {e}")
            return None
        
        if not comparison_result:
            print("Condition failed: first argument is NOT strictly greater than second.")
            return None

        # Condition met, execute the original function
        result = func(*args[2:], **kwargs)  # Pass remaining args to func
        return result
    
    return wrapper

if __name__ == '__main__':
    @is_strictly_greater
    def add(a, b):
        """Returns sum of a and b."""
        print(f"Adding {a} + {b}")
        return a + b

    # Test Case 1: First argument > Second (Should execute)
    result_1 = add(5, 3)
    
    # Test Case 2: First argument < Second (Should NOT execute body)
    print("--- Testing failure case ---")
    result_2 = add(3, 5)

    # Test Case 3: Equal arguments (Should NOT execute body)
    print("--- Testing equality case ---")
    result_3 = add(7, 7)

    print(f"Result from valid input: {result_1}")