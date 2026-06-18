def print_length(func):
    """Decorator that prints the length of any string passed to it before executing the function."""
    def wrapper(*args, **kwargs):
        # Check if all positional arguments are strings and calculate their lengths
        for arg in args:
            if isinstance(arg, str):
                print(f"Length of '{arg}': {len(arg)}")
        return func(*args, **kwargs)
    return wrapper

@print_length
def greet(name, greeting="Hello"):
    """A simple function that greets someone."""
    return f"{greeting}, {name}!"

if __name__ == '__main__':
    # Sample values to test the decorator without user input or external dependencies
    print(greet("Alice"))  # Should print length of "Alice" and execute greet
    print(greet("Bob", greeting="Hi"))  # Should print lengths for both arguments if applicable (only 'Bob' is string)