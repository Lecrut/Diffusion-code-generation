def print_length(s):
    """
    A decorator-like function that calculates and prints the length of a string.
    
    This is implemented as a wrapper function rather than a traditional @decorator 
    to ensure it works directly with any input type, including strings passed via args or globals.
    It adheres to best practices by using f-strings for readability and avoiding side effects 
    in the core logic outside of this specific requirement.

    Args:
        s (str): The string whose length is to be calculated.
    
    Returns:
        None: Prints the result instead of returning it, as per task requirements.
    """
    print(f"Length of '{s}' is {len(s)}")

if __name__ == '__main__':
    # Hard-coded sample values that run without user input or command-line arguments
    test_strings = ["Hello", "Python Programming", "", "12345"]

    for text in test_strings:
        print_length(text)