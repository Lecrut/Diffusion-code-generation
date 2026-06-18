def print_length(func):
    """Decorator that calculates and prints the length of a string passed to the function."""
    def wrapper(*args, **kwargs):
        # Get all positional arguments (assuming at least one is expected)
        if not args:
            raise TypeError("print_length requires at least one argument.")

        value = args[0]
        
        # Check if the first argument is a string-like object with __len__ method
        try:
            length = len(value)
        except TypeError as e:
            print(f"Error: The provided argument must be a string or sequence. {e}")
            return

        result = func(*args, **kwargs)
        
        # Print the length after execution
        if isinstance(result, str):
            print(f"The length of '{value}' is {length}.")
            
    return wrapper

# Sample block with hard-coded values to test the decorator
if __name__ == '__main__':
    @print_length
    def greet(name: str) -> str:
        """Returns a greeting message."""
        return f"Hello, {name}!"

    # Test cases without user input or command-line arguments
    print("Test 1:")
    result = greet("Alice")
    
    print("\nTest 2:")
    result = greet("Bob")