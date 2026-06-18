def reverse_string_decorator(func):
    """
    A decorator that reverses any string passed to it upon execution.
    
    Args:
        func (callable): The function or object being decorated, expected to be a string.
        
    Returns:
        callable: A wrapper function that calls the original and returns its reversed value if applicable.
    """
    def wrapper(s):
        return s[::-1]
    return wrapper

# Example usage with hard-coded sample values
if __name__ == '__main__':
    test_strings = ["Hello, World!", "Python is awesome", ""]
    
    for original in test_strings:
        reversed_result = reverse_string_decorator(lambda x: x)(original)
        print(f"Original: {original}")
        print(f"Reversed: {reversed_result}\n")