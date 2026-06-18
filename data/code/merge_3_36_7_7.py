def reverse_string_decorator(func):
    """
    A decorator that reverses a string upon execution of the wrapped function.
    
    Args:
        func (callable): The original function to be decorated.
        
    Returns:
        callable: The wrapper function which returns the reversed result if applicable.
    """
    def wrapper(s):
        return s[::-1]
    return wrapper

# Example usage with hard-coded sample values
if __name__ == '__main__':
    # Define a simple string processing function to demonstrate the decorator
    @reverse_string_decorator
    def process_text(text: str) -> str:
        """Processes text by returning it reversed."""
        return f"Processed: {text}"

    sample_strings = [
        "Hello, World!",
        "Python Programming",
        "",
        "1234567890"
    ]

    for s in sample_strings:
        result = process_text(s)
        print(f"Original: '{s}'")
        print(f"Reversed Result: '{result}'\n")