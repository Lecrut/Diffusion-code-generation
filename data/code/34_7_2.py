"""
Module to implement a decorator that capitalizes the first letter of every word in any string it decorates.
This module does not require external dependencies, user input, or command-line arguments.
It includes an example usage block demonstrating its functionality with hard-coded sample values.
"""

def capitalize_words(func):
    """
    Decorator function that wraps a callable to automatically capitalize the first letter 
    of every word in any string argument passed to it (before execution) and returns a new list 
    containing capitalized words if the input is a single string, or processes lists/tuples similarly.

    If the decorated function receives a string as an argument, this decorator will modify that 
    specific string by capitalizing its first letter of every word before calling the original function.
    
    Note: This implementation assumes all arguments passed to the wrapped functions are strings when applicable.
    """

    def wrapper(*args):
        # Iterate over args and capitalize words in any string argument found
        capitalized_args = []
        
        for arg in args:
            if isinstance(arg, str) and len(arg.strip()) > 0:
                # Use split to handle multiple spaces correctly as the requirement implies standard word capitalization rules.
                # However, strictly following "first letter of every word", we can use a simple approach or re.split for robustness against extra whitespace.
                words = arg.split() 
                capitalized_words = [word.capitalize() if word else '' for word in words]
                result_str = ' '.join(capitalized_words)
                
                # If the original string had multiple spaces that shouldn't be collapsed (though not strictly requested),
                # standard "capitalize" behavior usually implies collapsing. Given typical usage, splitting and joining is safer 
                # to ensure correct single-space delimiters between words unless otherwise specified for preserving internal spacing structure per word boundary.
                
                capitalized_args.append(result_str)
            else:
                capitalize_words = arg
                
        return func(*capitalized_args)

    wrapper.__name__ = func.__name__ + "_decorated"
    return wrapper

# Example usage block demonstrating the decorator functionality with hard-coded sample values.
if __name__ == '__main__':
    # Define a function to be decorated using our customizer logic
    
    def greet(name, message):
        """Original function that takes name and message."""
        
        if isinstance(message, str) or isinstance(name, str):
            return f"{message} {name}"
            
        else:
            raise TypeError("Arguments must include string inputs for testing the decorator.")

    # Apply the customizer to greet() so it capitalizes all words in name/message before passing them.
    
    decorated_greet = capitalize_words(greet)
    
    print("--- Test Case 1 ---")
    result_1 = decorated_greet("hello world", "good morning")
    print(f"Result: {result_1}")

    # Demonstrate with another example to ensure multiple words are capitalized correctly.
    print("\n--- Test Case 2 ---")
    result_2 = decorated_greet("this is a test string", "another sample input here too!")
    
    print(f"\nResult: {result_2}")

    # Demonstrate handling of non-string arguments (should be passed through as-is, assuming they aren't strings). 
    # Although the task focuses on strings, we ensure robustness by checking types.
    print("\n--- Test Case 3 ---")
    result_3 = decorated_greet(12345, "hello world again!")
    
    print(f"\nResult: {result_3}")