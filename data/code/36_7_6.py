def reverse_string_decorator(func):
    """
    A decorator that reverses a string upon execution of the wrapped function.
    
    Args:
        func (callable): The original function to be decorated.
        
    Returns:
        callable: The wrapper function which returns the reversed result if input is a string, 
                  otherwise it calls and returns the original function's output unchanged.
    """
    def wrapper(*args, **kwargs):
        # Check if any positional argument is a string or if there are keyword arguments that might be strings
        has_string_arg = False
        
        for arg in args:
            if isinstance(arg, str):
                has_string_arg = True
                break
                
        for key, value in kwargs.items():
            if isinstance(value, str):
                has_string_arg = True
                break
        
        # If a string argument is found and it's the first positional arg (common use case), reverse it.
        # For simplicity, we assume the decorator works on the first positional argument 
        # or any keyword argument that is a string by reversing all strings in the arguments tuple/dict representation?
        # To strictly follow "applied to any string", let's identify if ANY input contains a string and reverse it.
        
        result = func(*args, **kwargs)
        
        # If the function returns a single string or one of its inputs was reversed, we need logic here.
        # However, decorators usually wrap functions that return values. 
        # The prompt says "applied to any string... automatically reversing". 
        # This implies if the input is a string, reverse it before passing? Or after getting result?
        # Let's assume: If the function receives a string as an argument (e.g., `reverse_text(text)`), return reversed text.
        
        # Re-evaluating based on typical decorator usage for strings: 
        # Usually, we want to transform the input or output. Given "reversing upon execution", 
        # it likely means if the function processes a string, make sure that string is returned reversed.
        # But since decorators wrap functions, and we don't know what func does internally without calling it:
        
        # A safer interpretation for a general decorator on strings passed to any function:
        # If ANY argument in args or kwargs is a string, reverse THAT specific string? 
        # Or if the result of func() is a string, return reversed(result)?
        
        # Let's go with: If the output of `func` is a single string, return its reversal.
        # This covers cases like def greet(name): ... returning name or greeting text.
        
        if isinstance(result, str) and len(result) > 0:
            return result[::-1]
            
        return result

    return wrapper

def reverse_text(text):
    """Example function that takes a string."""
    # Simulating some processing (e.g., uppercasing) before returning the original text logic for demonstration
    processed = "Processed: " + text.upper()
    return processed

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python"]
    
    print("Original:", reverse_text(sample_strings[0]))
    # The decorator is applied to the function definition above. 
    # Since we defined it without @reverse_string_decorator in this specific example block,
    # let's demonstrate usage by applying it manually or redefining with the decorator for clarity if needed?
    
    # To strictly follow "Design and implement a decorator... Return only code", I will apply it to reverse_text here.
    decorated_reverse = reverse_string_decorator(reverse_text)

    print("Reversed via Decorator:", decorated_reverse(sample_strings[0]))