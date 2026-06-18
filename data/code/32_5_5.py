import functools

def print_string_length(func):
    """
    Decorator that prints the length of any string passed to the wrapped function,
    then executes the original function with its arguments unchanged.

    This decorator is designed to work specifically when a string argument is provided.
    If no string or non-string types are involved in a way relevant here, it simply runs normally.
    
    Args:
        func (callable): The function to decorate.
        
    Returns:
        callable: A wrapper that prints the length of any string arguments before calling `func`.

    Example usage:
        @print_string_length
        def greet(name):
            return f"Hello, {name}!"
    
        print(greet("Alice"))  # Output: Length is 5. Hello, Alice!
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        string_args = [arg for arg in args if isinstance(arg, str)]
        
        if any(isinstance(a, str) for a in args):
            print(f"Length is {len(string_args[0])}.")

        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    @print_string_length
    def greet(name):
        """Greets the user."""
        return f"Hello, {name}!"

    @print_string_length
    def describe_city(city):
        """Describes a city briefly."""
        description = "A vibrant metropolis known for its culture." if len(city) > 5 else "A small town with charm."
        return f"{city}: {description}"

    # Hard-coded sample values to demonstrate functionality without user input.
    print(greet("Alice"))
    print(describe_city("Paris"))
    print(describe_city("Town"))