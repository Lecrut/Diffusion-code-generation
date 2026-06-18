def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(*args, **kwargs):
        # Ensure there are at least two positional arguments to compare
        if len(args) < 2:
            raise TypeError("is_strictly_greater requires at least two positional arguments")
        
        a = args[0]
        b = args[1]

        # Check condition strictly greater than
        if not (a > b):
            return None
        
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__
    return wrapper

if __name__ == '__main__':
    @is_strictly_greater
    def greet(name, age):
        """A simple function that greets based on name and age."""
        if isinstance(age, int) and 0 <= age:
            return f"Hello {name}, you are {age} years old."
        else:
            raise ValueError("Age must be a non-negative integer.")

    # Test cases with hard-coded values
    print(greet("Alice", 25))      # Should execute (25 > ? No, wait logic check)
    
    # Correction in usage for the decorator to work as intended per task description:
    # The task says "first argument is strictly greater than second". 
    # So we need a function that takes two comparable args where arg0 > arg1.
    
    @is_strictly_greater
    def compare_values(x, y):
        return f"x={x}, y={y}, x>y condition met"

    result = compare_values(5, 3)   # Should execute (5 > 3) -> "compare_values called" logic inside if needed or just print
    print(result)                   # Output: compare_values(5, 3), x>... 

    # Another test where it should NOT execute due to condition failure
    result2 = compare_values(4, 6)   # Should not execute (4 is not > 6) -> returns None
    
    # Test with string comparison if applicable or just numbers for simplicity here. 
    # Let's assume numeric context as per typical strict greater examples unless specified otherwise.
    
    print("Execution complete.")