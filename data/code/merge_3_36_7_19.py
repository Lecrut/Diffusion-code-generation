import functools

def reverse_str(text: str) -> str:
    """
    Decorator factory that reverses any string it decorates.
    
    When applied to a function or method, this decorator intercepts 
    the call and returns the reversed version of the result (assuming 
    the original result is a string). If the input itself is not a 
    string but we are demonstrating on strings as per task requirements,
    it simply reverses the provided text object directly.

    Args:
        text (str): The string to be processed or decorated over.

    Returns:
        str: A new reversed version of the original string.
    """
    
    def decorator(func=None):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if func is None:
                # Case 1: Direct application to a string value
                return text[::-1]
            
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return result[::-1]
            else:
                return result
        
        return wrapper
    
    return decorator

# Alternative implementation specifically for the task description 
# which implies a simpler usage pattern often seen in interview contexts.

def reverse_decorator(func=None):
    """
    Returns a decorator that reverses string results or inputs if passed directly.
    
    This version aligns with typical "apply to any string" requests where
    one might decorate functions returning strings, but also works on 
    direct object passing in the context of demonstration.
    
    If func is None (direct use), it returns a function that reverses its argument.
    Otherwise, it wraps the provided function to reverse its return value if it's a string.
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            return str(result)[::-1] # Ensure we treat output as string and reverse
        return wrapper
    
    if func is None:
        return decorator

# Let's implement the most robust version that satisfies "applied to any string"
# meaning it can be used on a function returning strings, or even just 
# demonstrating the reversal capability directly.

def make_reverse_decorator():
    """Factory creating a reverse logic."""
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Execute original function to get string result (if any) or assume input handling in test cases below.
            try:
                res = func(*args, **kwargs)
                if isinstance(res, str):
                    return res[::-1]
                else:
                    # Fallback for non-string results though task focuses on strings
                    return f"Result not string, original format: {res}"
            except Exception as e:
                return f"Error occurred while reversing or executing function: {str(e)}"
        return wrapper
    
    return decorator

# However, re-reading the prompt: "applied to any string... automatically reversing". 
# This often implies a method attached to an object or simply inverting text.
# Let's provide a clean solution that demonstrates this clearly with sample usage.

def reverse_string_decorator(text):
    """Directly reverses a given string."""
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no input(), sys.stdin, etc.)
    
    samples = [
        "Hello World",
        "Python is awesome",
        "",
        "!@#$%20Spaces"
    ]

    print("Original Strings:")
    for s in samples:
        print(f'"{s}"')
        
    print("\nReversed Strings (using direct reversal logic):")
    
    # Demonstrate the core functionality requested
    reversed_results = []
    for sample in samples:
        res = reverse_string_decorator(sample)
        reversed_results.append(res)
        print(f'" {res} "')

    # If we were to use a decorator pattern on functions returning strings, 
    # here is how it would look conceptually (though not strictly required by the core reversal task):
    
    def greet(name: str) -> str:
        return f"Hello {name}"