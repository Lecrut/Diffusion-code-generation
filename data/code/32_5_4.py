def print_length(func):
    """Decorator that calculates and prints the length of any string argument passed to a function."""
    def wrapper(*args, **kwargs):
        # Identify which arguments are strings by checking their type at runtime
        for arg in args:
            if isinstance(arg, str):
                func_len = len(arg)
                print(f"String '{arg}' has length {func_len}")
        
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__  # Preserve function name
    return wrapper

# Sample usage block with hard-coded values to ensure the module runs without user input or external dependencies.
if __name__ == '__main__':
    @print_length
    def greet(name):
        print(f"Hello, {name}!")
    
    test_strings = ["Alice", "Bob Smith", "", "Python is great"]

    # Calling the decorated function with sample strings
    greet("World")
    greet(test_strings[0])
    greet(test_strings[1])