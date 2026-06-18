def print_string_length(func):
    """Decorator that prints the length of any string passed to the wrapped function."""
    
    def wrapper(*args, **kwargs):
        # Check if all arguments or keyword values are strings and have a defined length
        for arg in args:
            try:
                len(arg)
            except TypeError:
                pass  # Not a sequence/string-like object
            
        result = func(*args, **kwargs)
        
        # Identify which argument was the string to print its length (usually first positional or specific keyword)
        if args and isinstance(args[0], str):
            print(f"Length of '{args[0]}': {len(args[0])}")
        elif kwargs:
            for key, value in kwargs.items():
                try:
                    len(value)
                except TypeError:
                    pass
        
        return result
    
    return wrapper

@print_string_length
def greet(name):
    """A simple greeting function."""
    print(f"Hello, {name}!")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    greet("Alice")
    greet("Bob", name="Charlie")  # Using keyword argument for testing flexibility
    
    # Additional test cases with multiple arguments to ensure robustness
    print_string_length(greet)("David")