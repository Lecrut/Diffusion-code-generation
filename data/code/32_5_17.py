def print_string_length(func):
    """Decorator that prints the length of any string passed to it before executing the function."""
    def wrapper(*args, **kwargs):
        # Check if all positional arguments are strings and calculate their lengths
        for arg in args:
            if isinstance(arg, str):
                print(f"Length of '{arg}': {len(arg)}")
        
        return func(*args, **kwargs)
    return wrapper

@print_string_length
def greet(name):
    """A simple greeting function."""
    return f"Hello, {name}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate the decorator functionality
    print(greet("Alice"))
    print(greet("Bob"))