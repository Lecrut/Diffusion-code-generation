def string_length_decorator(func):
    """
    A decorator that prints the length of any string passed to its arguments 
    before calling the original function. It handles both single strings 
    as a positional argument or within other data structures if applicable, 
    but primarily targets direct string passing based on typical usage patterns.

    This implementation assumes the decorated function accepts at least one 
    argument that could be a string. If multiple arguments are passed and only 
    one is expected to trigger this check (e.g., first positional), it checks that specific one.
    
    Note: To keep scope minimal as per 'best practices' for such tasks without over-engineering,
    we assume the function being decorated takes at least one argument which will be checked if isinstance(string).

    Args:
        func: The original function to decorate.
        
    Returns:
        A wrapper function that prints string lengths before executing `func`.
    """
    def wrapper(*args, **kwargs):
        # Check arguments for strings and print their lengths
        for arg in args:
            if isinstance(arg, str):
                length = len(arg)
                print(f"Length of argument '{arg[:10]}...' is {length}")  # Truncate long strings for readability
        
        return func(*args, **kwargs)

    return wrapper

@string_length_decorator
def greet(name: str, greeting: str = "Hello"):
    """A simple function demonstrating the decorator."""
    print(f"{greeting}, {name}!")
    return name + "!"

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    
    greet("Alice", greeting="Hi")
    
    result = greet("Bob")
    
    long_name = "This is a very long string that should be truncated in the output"
    greet(long_name)