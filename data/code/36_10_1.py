def reverse_string(s: str) -> str:
    """
    Reverses a given string using Python's slicing syntax, which is efficient 
    and concise (Pythonic).
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of the original string in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction or file I/O needed.
    samples = ["Hello, World!", "Python is great", "!gnivelpoc"]
    
    for test_input in samples:
        reversed_output = reverse_string(test_input)
        print("Original:", repr(test_input))
        print("Reversed:", repr(reversed_output))
        print("-" * 30)