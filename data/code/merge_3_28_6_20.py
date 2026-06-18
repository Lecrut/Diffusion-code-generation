def is_strictly_greater(func):
    """Decorator that ensures the first argument is strictly greater than the second before execution."""
    def wrapper(*args, **kwargs):
        if len(args) >= 2:
            a = args[0]
            b = args[1]
            # Ensure both arguments are comparable (numbers)
            try:
                if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                    raise TypeError("Arguments must be numeric.")
                if not a > b:
                    print(f"Skipping execution because {a} is not strictly greater than {b}.")
                    return None  # Or could return a specific value indicating skipping
            except TypeError as e:
                print(f"Error during comparison: {e}")
                return None
        
        return func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    @is_strictly_greater
    def add(x, y):
        """Returns the sum of x and y."""
        return x + y

    # Test case 1: First argument is strictly greater than second (should execute)
    result_1 = add(5, 3)
    
    # Test case 2: First argument equals second (should not execute logic inside function based on prompt requirement interpretation, 
    # though the decorator checks strict inequality. The wrapper returns None here if condition fails.)
    result_2 = add(4, 4)

    # Test case 3: First argument is less than second (should not execute logic inside function)
    result_3 = add(3, 5)

    print(f"Result of add(5, 3): {result_1}")
    
    if result_2 is None:
        print("add(4, 4) was skipped as per decorator rules.")
    else:
        print(f"Result of add(4, 4): {result_2}")

    if result_3 is None:
        print("add(3, 5) was skipped as per decorator rules.")
    else:
        print(f"Result of add(3, 5): {result_3}")