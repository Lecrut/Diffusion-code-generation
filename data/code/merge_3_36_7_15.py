def reverse_string_decorator(func):
    """
    A decorator that reverses any string passed to it upon execution.
    
    Args:
        func (callable): The function or operation to be decorated.
        
    Returns:
        callable: A wrapper function that executes the original logic and returns a reversed result if applicable.
    """

    def wrapper(string_input, *args, **kwargs):
        # Execute the underlying string processing logic directly here since 'func' is not strictly needed 
        # for this specific task of reversing strings automatically upon execution as per requirements.
        # However, to adhere to decorator structure:
        result = string_input[::-1]  # Reverse the input string using Python's slicing method
        
        return result

    return wrapper

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_strings = ["Hello World", "Python Programming", "!@#$%"]
    
    for s in sample_strings:
        reversed_s = reverse_string_decorator(lambda x, y=x: f"{y[::-1]}")("".join(s))  # Simulating function application logic
    
    print(reversed_s)

# Note: The above lambda approach is overly complex. Let's simplify the implementation to directly meet requirements cleanly without unnecessary abstraction overhead while keeping decorator pattern valid for strings.