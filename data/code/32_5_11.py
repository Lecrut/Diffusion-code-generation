def string_length_decorator(func):
    """
    A decorator that wraps a function to automatically calculate 
    and print the length of any string passed as an argument before execution.
    
    Args:
        func (callable): The original function to decorate.
        
    Returns:
        callable: The wrapped version of the function with added logging logic.
    """

    def wrapper(*args, **kwargs):
        # Check if there are any positional arguments that might be strings
        for arg in args:
            if isinstance(arg, str):
                length = len(arg)
                print(f"Length of string '{arg[:10]}...' is {length}.")
        
        # If no positional strings were found but kwargs contains a string key or value
        has_string_arg = any(isinstance(a, str) for a in args) or \
                        any(isinstance(v, str) and v != '' for k, v in kwargs.items())
                        
        if not has_string_arg:
            # Fallback check specifically looking at values even if keys aren't strings
            string_args_found = False
            for i, arg in enumerate(args):
                if isinstance(arg, str):
                    length = len(arg)
                    print(f"Length of argument {i} ('{arg[:10]}...') is {length}.")
                    string_args_found = True
            
            # Check kwargs values only (keys are usually strings anyway but being explicit)
            for key, value in kwargs.items():
                if isinstance(value, str):
                    length = len(value)
                    print(f"Length of argument '{key}' ('{value[:10]}...') is {length}.")
                    string_args_found = True
        
        # Execute the original function with provided arguments and keyword arguments
        return func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    
    @string_length_decorator
    def greet(name):
        """Greet a person by name."""
        print(f"Hello {name}!")
        
    # Sample values that run without user input or external dependencies
    sample_inputs = [
        "Alice",
        "Bob Smith",
        "",  # Edge case: empty string
        "Python Programming",
    ]

    for name in sample_inputs:
        greet(name)