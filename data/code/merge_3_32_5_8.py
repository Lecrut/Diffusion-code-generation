def measure_length(func):
    """Decorator that calculates and prints the length of a string argument passed to the wrapped function."""
    
    def wrapper(*args, **kwargs):
        # Find all positional arguments in case they are strings or keyword args if applicable (though task implies 'any string')
        # For simplicity based on "passed to it", we assume primary positional arg is the target. 
        # If multiple args exist, this logic targets index 0 as per common usage patterns for such tasks unless specified otherwise.
        input_string = None
        
        if len(args) > 0:
            input_string = args[0]
        
        elif any(isinstance(arg, str) for arg in kwargs.values()):
            # Fallback to first string keyword argument found
            for val in kwargs.values():
                if isinstance(val, str):
                    input_string = val
                    break
        
        if input_string is not None:
            length = len(input_string)
            print(f"Length of '{input_string}': {length}")

        return func(*args, **kwargs)
    
    return wrapper

if __name__ == '__main__':
    @measure_length
    def greet(name):
        """Greets the user."""
        return f"Hello, {name}!"

    # Hard-coded sample values as per requirements (no input(), sys.stdin, argparse required)
    print(greet("Alice"))          # Output: Length of 'Alice': 5 ... Hello, Alice!
    print(greet("Bob Johnson"))   # Output: Length of 'Bob Johnson': 12 ... Hello, Bob Johnson!
    
    # Additional test with keyword argument if the function signature supported it dynamically 
    # (though current implementation assumes positional for simplicity unless multiple strings exist)
    # To demonstrate robustness without breaking the single runnable module constraint:
    
    @measure_length
    def describe(item):
        return f"The item is {item}."

    print(describe("Python"))      # Output: Length of 'Python': 6 ... The item is Python.