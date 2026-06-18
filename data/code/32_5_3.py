import functools

def print_string_length(func):
    """
    A decorator that wraps a function to automatically calculate 
    and print the length of any string passed as an argument before execution.
    
    Args:
        func (callable): The original function to decorate.
        
    Returns:
        callable: The wrapped function with added side-effect behavior.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Identify string arguments by checking type at runtime
        for arg in args:
            if isinstance(arg, str):
                print(f"Length of '{arg}' is {len(arg)}")
        
        return func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    
    @print_string_length
    def greet(name):
        """Greet a person by name."""
        return f"Hello, {name}!"

    @print_string_length
    def describe_city(city):
        """Describe a city using its name."""
        return f"The capital of France is {city}, known for the Eiffel Tower."

    
    result1 = greet("Alice")
    print(f"Greeting returned: {result1}")
    
    result2 = describe_city("Paris")
    print(f"Description returned: {result2}")