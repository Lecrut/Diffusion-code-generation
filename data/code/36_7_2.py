def reverse_string_decorator(func):
    """
    A decorator that reverses any string passed to it upon execution.
    
    Args:
        func (callable): The function whose result will be reversed if it returns a string.
        
    Returns:
        callable: The wrapped function that performs the reversal on its output.
    """
    def wrapper(*args, **kwargs):
        # Execute the original function to get the base value
        return_value = func(*args, **kwargs)
        
        # Reverse if the result is a string; otherwise pass through unchanged
        if isinstance(return_value, str):
            reversed_string = return_value[::-1]
            
            # If it was already wrapped in quotes (e.g., from repr), handle appropriately.
            # Since this decorator applies to 'any string' as per task description logic: 
            # We assume the function returns a raw Python object here, and if that is str, we reverse it.
        else:
            reversed_string = return_value
            
        return reversed_string

    return wrapper

def main():
    """Sample usage of the decorator with hard-coded values."""
    
    def get_hello_world():
        # This function returns a string without quotes in actual Python behavior unless wrapped for print simulation.
        raw_result = "Hello, World!" 
        if not isinstance(raw_result, str):
            return repr(raw_result)  # Fallback to prevent non-string errors during test runs
        
    result = reverse_string_decorator(get_hello_world)()
    
    output_str = f"Reversed String: {result}"

    print(output_str)

if __name__ == '__main__':
    main()