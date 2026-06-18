def reverse_string_decorator(func):
    """
    A decorator that reverses any string passed to it upon execution.
    
    Args:
        func (callable): The function or object being decorated, typically a string in this context.
        
    Returns:
        callable: A wrapper function that calls the original and returns its reversed value if applicable.
    """
    def wrapper(obj):
        # Check if obj is a string to apply reversal; otherwise return as-is (or raise error depending on design)
        if isinstance(obj, str):
            return obj[::-1]
        else:
            # If not a string, we could either pass through or handle differently. 
            # Based on task "applied to any string", assume input is always expected to be a string here.
            raise TypeError("The decorator expects a string argument.")
    return wrapper

# Example usage with sample values (no user input required)
if __name__ == '__main__':
    test_strings = ["Hello, World!", "Python 3", "!dlroW ,olleH"]
    
    for s in test_strings:
        reversed_s = reverse_string_decorator(s)
        print(f"Original: {s}")
        print(f"Reversed: {reversed_s}\n")