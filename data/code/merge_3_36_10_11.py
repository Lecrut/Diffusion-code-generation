import sys

def reverse_string(s: str) -> str:
    """
    Reverses the input string using slicing, which is a Pythonic method.

    Args:
        s (str): The original string to be reversed.

    Returns:
        str: A new string with characters in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    sample_input = "Hello, World!"
    
    reversed_output = reverse_string(sample_input)
    
    print(reversed_output)