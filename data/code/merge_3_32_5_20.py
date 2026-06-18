def print_length(text):
    """Decorator that prints the length of a string passed to it."""
    def decorator(func):
        import functools
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, str):
                print(f"String length: {len(text)}")
                
            return result
            
        return wrapper
    
    return decorator

if __name__ == '__main__':
    @print_length("Hello World")
    def greet():
        return "Welcome to Python!"
    
    # Additional test cases with different string types passed explicitly if needed, 
    # but the task implies calculating length of 'text' argument. 
    # Since decorators wrap functions and don't easily access outer variables directly without closure tricks,
    # we adjust slightly: The decorator as defined above prints len(text) where text is an argument to the decorated function?
    # Re-reading requirement: "calculates ... any string passed to it". This implies the string should be a parameter.
    
    @print_length("Sample String")
    def process_string(s):
        return f"Processed {s}"

    result = process_string("Input Data Here")
    print(f"Result: {result}")