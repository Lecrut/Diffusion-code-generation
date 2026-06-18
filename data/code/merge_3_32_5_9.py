def print_length(func):
    """Decorator that prints the length of any string passed to it before executing the function."""
    def wrapper(*args, **kwargs):
        # Check if the first argument is a string and get its length
        if args:
            arg = args[0]
            try:
                len(arg)  # Trigger TypeError if not subscriptable or check type implicitly via usage below
            except (TypeError, AttributeError):
                pass
            
            if isinstance(arg, str):
                print(f"Length of string '{arg}': {len(arg)}")
        
        return func(*args, **kwargs)

    return wrapper

@print_length
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    test_strings = ["Alice", "Bob", "", "Python 3.10"]

    for s in test_strings:
        result = greet(s)
        print(result)