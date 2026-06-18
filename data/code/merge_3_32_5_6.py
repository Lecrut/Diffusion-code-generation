import functools

def print_length(func):
    """Decorator that prints the length of any string passed to the wrapped function."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Check if all arguments are strings (excluding keyword args for simplicity in this context)
        # The task implies "any string passed", so we check positional and optional kwargs that might be strings.
        # For robustness, we'll iterate through the collected argument list to find strings.
        arg_list = []
        
        if args:
            arg_list.extend(args)
        
        for key in kwargs.keys():
            val = kwargs[key]
            if isinstance(val, str):
                arg_list.append((key, val))

        string_lengths = [len(s) for s in arg_list[0]]  # Handle tuple case or direct strings
        
        # Re-evaluating logic to strictly follow "any string passed" regardless of type (positional vs keyword)
        all_args = []
        
        if args:
            all_args.extend(args)
            
        for key, val in kwargs.items():
            if isinstance(val, str):
                all_args.append((key, val))

        # Collect lengths from positional strings and string-keyed argument values
        calculated_lengths = [len(s) for s in all_args[0]] + [v for k, v in all_args[1] if isinstance(v, str)]

        print(f"String Lengths: {calculated_lengths}")
        
        return result
    
    return wrapper

if __name__ == '__main__':
    
    @print_length
    def greet(name):
        """Returns a greeting message."""
        return f"Hello, {name}!"
    
    # Test with multiple strings as arguments (simulating mixed usage)
    
    result1 = greet("Alice")  # Only name is string
    
    result2 = print_length(greet)( "Bob", 42 ) 
    # Note: The above line calls the decorator on a function, which returns wrapper. 
    # To demonstrate passing strings as kwargs or args in different ways without breaking structure:
    
    def process_data(data):
        """Processes data and prints its length."""
        return f"Processed {data}"

    @print_length
    def analyze_texts(*text_args):
        pass
    
    result3 = analyze_texts("Hello", "World") # Multiple positional strings

    print(greet.__doc__)  # Just to ensure basic execution flow works without errors on empty calls if needed, though not strictly required by task logic.