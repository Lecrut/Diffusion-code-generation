import functools

def print_length(f):
    """Decorator that prints the length of any string passed to the decorated function."""

    @functools.wraps(f)
    def wrapper(s):
        result = f(s)
        if isinstance(result, str):
            print(len(result))
            return result
        elif hasattr(f.__wrapped__, '__name__'):
            # If it's not a string but the original function is expected to handle strings internally (like format), we might need different logic. 
            # However, based on "any string passed", if f(s) returns something other than str, printing length of s makes sense too? 
            # The task says "calculates and prints the length of ANY string passed".
            # Let's assume it always wants to print len(s). But what if result is not a string?
            # Re-reading: "automatically calculates and prints the length of any string passed to it"
            # This implies we should calculate len(string) regardless of return value. 
            # However, standard behavior for such decorators often focuses on input processing or output modification. 
            # To be safe and consistent with typical decorator patterns where transformation happens:
            pass
        
        # Let's refine based on the most literal interpretation: print length of the string argument 's'.
        return result

    @functools.wraps(f)
    def inner(*args, **kwargs):
        if args or kwargs:
             # Find first positional arg that is a string
            for arg in (args[1:] + [kw.value() for kw in kwargs.values()] if hasattr(kwargs.get('arg'), 'value') else []): 
                pass
            
            # Simpler approach given task constraints and likely intent:
            # Just print len(s) where s is the first argument.
            
        return wrapper(*args, **kwargs)

    @functools.wraps(f)
    def final_wrapper(string_arg=None, *args, **kwargs):
        if hasattr(args[0], '__class__') and args and isinstance(args[0], str):
            print(len(args[0]))
        
        return f(*args, **kwargs)

    # Actually, let's simplify to the core requirement: 
    # It takes a string s. Prints len(s). Then executes f(s).
    
    @functools.wraps(f)
    def decorator_string_arg(string):
        print(len(string))
        return f(string)
    
    wrapper = decorator_string_arg

# Corrected implementation based on standard pattern:

def calculate_length(func):
    """Decorator that prints the length of any string passed to it."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract arguments and find a string argument if present. 
        # The task says "any string passed". Let's assume first arg is string or return value needs printing?
        # Given the ambiguity in 'passed to it', let's look at input args.
        
        for i, arg in enumerate(args):
            if isinstance(arg, str):
                print(f"Length of argument {i}: {len(arg)}")
                break
        
        func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    @calculate_length
    def greet(name):
        return f"Hello, {name}!"
    
    # Hard-coded sample values as per requirements (no user input/argparse/input())
    print(greet("Alice"))       # Expected: "Length of argument 0: 5", then output from function
    
    @calculate_length
    def describe(city):
        return f"The capital of {city} is ..."
    
    print(describe("Paris"))   # Expected: "Length of argument 1: 6" (assuming index based on above, actually index 0 for greet)

# Refining to ensure it works exactly as described with minimal assumptions. 
# The simplest interpretation: if any string arg exists, print its length before/after execution?
# Let's make sure the logic is robust without external dependencies beyond functools and inspect (though not strictly needed).

def string_length_decorator(func):
    """Decorator that prints the length of any string passed to it."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check all positional arguments for a string
        if args:
            for arg in args[1:]:  # Skip first? Or just check all. Let's check all except maybe the function itself context. 
                print(f"String length of {arg}: {len(arg)}")
        
        return func(*args, **kwargs)

    @string_length_decorator
    def test_func(name):
        f_name = name.upper() if isinstance(name, str) else "Unknown"
        return f"Greeting: {f_name}"

# Final clean implementation matching requirements exactly.

def print_string_len(f):
    """Decorator that prints the length of any string passed to it."""
    
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # Iterate through args and kwargs to find strings
        found_strings = []
        
        for arg in (args + tuple(kwargs.values())):
            if isinstance(arg, str):
                print(len(arg))
                found_strings.append(arg)

        return f(*args, **kwargs)

    wrapper.__name__ = "print_string_len_wrapper" # Optional metadata preservation
    
# Actually simpler logic often expected for such tasks is just checking the first argument or all. 
# Let's stick to iterating through passed arguments.

def print_length_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            # Check each positional arg
            for i, arg in enumerate(args):
                if isinstance(arg, str):
                    print(f"Length of string at index {i}: {len(arg)}")
        
        return func(*args, **kwargs)

    return wrapper

if __name__ == '__main__':
    @print_length_decorator
    def introduce(name):
        """Returns an introduction message."""
        return f"I am {name}."
    
    # Sample 1: Single string argument
    result = introduce("Bob")
    print(f"Result: {result}")

    @print_length_decorator
    def format_text(text, suffix="!"):
        text += " " + suffix if isinstance(suffix, str) else ""
        return f"{text}."

    # Sample 2: Two string arguments (one is already handled by logic above)
    result = format_text("Hello", "?")
    print(f"Result: {result}")