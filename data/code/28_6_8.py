from functools import wraps

def is_strictly_greater(func):
    """
    A decorator that ensures a function's first argument must be strictly greater 
    than its second argument before execution occurs. If not, it raises an exception.
    
    Args:
        func (callable): The original function to decorate.

    Returns:
        callable: A new wrapper function with the validation logic applied.
    """
    @wraps(func)
    def decorator(a, b):
        if a <= b:
            raise ValueError(f"First argument ({a}) must be strictly greater than second argument ({b}).")
        return func(a, b)
    
    return decorator

if __name__ == '__main__':
    # Sample function to test the decorator
    def add(x, y):
        """Returns sum of x and y."""
        return x + y

    @is_strictly_greater
    def subtract(x, y):
        """Subtracts y from x (valid only if x > y)."""
        return x - y
    
    try:
        result = add(10, 5)
        print(f"add(10, 5) = {result}")
        
        # Testing subtract with valid input (strictly greater condition met)
        diff = subtract(20, 10)
        print(f"subtract(20, 10) = {diff}")
    except ValueError as e:
        print(f"Error occurred during execution: {e}")

    # Demonstrate failure case explicitly with a controlled test
    try:
        invalid_result = subtract(5, 10)
    except ValueError:
        print("Correctly caught error for subtract(5, 10)")