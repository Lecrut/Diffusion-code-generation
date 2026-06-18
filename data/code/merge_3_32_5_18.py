import functools

def print_string_length(func):
    """
    Decorator that prints the length of any string passed to the wrapped function.
    
    This decorator wraps a target function with an additional step: before executing 
    the original logic, it checks if the first argument is a string and prints its length.
    It uses functools.wraps to preserve metadata like function name and docstring.
    
    Args:
        func (callable): The function to decorate. Should accept at least one positional argument.

    Returns:
        callable: A wrapped version of 'func' that includes the logging behavior.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args and isinstance(args[0], str):
            print(f"Length of '{args[0]}': {len(args[0])}")
        
        return func(*args, **kwargs)

    return wrapper

# Example usage within the module to demonstrate functionality without external dependencies.
@print_string_length
def greet_user(name: str) -> None:
    """Greet a user by name."""
    print(f"Hello {name}!")

if __name__ == '__main__':
    # Hard-coded sample values for testing; no input prompts or arguments required.
    
    test_strings = [
        "Python",
        "",
        "Data Science and AI",
        123,  # Non-string value to ensure decorator handles mixed types gracefully (prints nothing)
    ]

    print("Testing string length calculation:")
    for s in test_strings:
        greet_user(s if isinstance(s, str) else "")
    
    # Explicit call with a specific string to verify behavior.
    greet_user("Hello World")