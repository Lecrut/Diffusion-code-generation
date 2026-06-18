def print_length(func):
    """Decorator that prints the length of any string passed to it."""
    def wrapper(*args, **kwargs):
        result = func(*args)  # Call original function and get its return value
        
        if isinstance(result, str):
            print(f"Length: {len(result)}")
        
        return result
    
    return wrapper

@print_length
def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    messages = ["Python", "Beautiful is better than ugly.", "!@#$%", ""]
    
    for msg in messages:
        print("Input:", repr(msg))