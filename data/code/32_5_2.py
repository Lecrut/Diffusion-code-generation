def print_string_length(func):
    """Decorator that prints the length of any string passed to it before calling the function."""
    def wrapper(*args, **kwargs):
        # Check if all positional arguments are strings or a mix where at least one is being treated as input
        # For simplicity in this task, we assume the first argument intended for processing might be a string.
        # However, to strictly adhere to "any string passed", let's inspect args and kwargs.
        
        lengths = []
        if len(args) > 0:
            arg_strs = [a for a in args if isinstance(a, str)]
            if arg_strs:
                lengths.extend(len(s) for s in arg_strs)
            
            # If there are keyword arguments that might be strings (though less common as primary input here)
            kwarg_strs = [(k, v) for k, v in kwargs.items() if isinstance(v, str)]
            if kwarg_strs:
                lengths.extend(len(s) for _, s in kwarg_strs)

        # If no strings were found but the function is expected to take a string (common pattern), 
        # this decorator might need context. But per task "any string passed", we just print what we find.
        
        if not arg_strs and not kwarg_strs:
            # Fallback logic often implies looking for specific input, but strictly following instructions:
            # If no strings are explicitly found in args/kwargs as primary inputs to this decorator's scope, 
            # it won't print anything unless the function itself passes a string internally or we assume first arg.
            # To make it useful and robust without over-engineering assumptions about which arg is input:
            pass

        if lengths:
            total_length = sum(lengths)
            print(f"String length(s): {total_length}")

        return func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    # Sample values hard-coded to ensure no user input or external dependencies are needed.
    
    @print_string_length
    def greet(name: str) -> None:
        print(f"Hello {name}!")

    @print_string_length
    def describe_product(product_name: str, description: str) -> None:
        # This function takes two strings; the decorator will check both.
        pass
    
    # Test cases with hard-coded sample values
    greet("Alice")
    
    describe_product("Widget", "A useful gadget for daily tasks.")