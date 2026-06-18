def reverse_word(s: str) -> str:
    """
    Reverses a single string using slicing for maximum efficiency.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed version of the input string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_strings = ["hello", "Python 3.9", "!olleh"]
    
    print("Original String: hello")
    print(f"Reversed String: {reverse_word('hello')}")
    
    print("\nOriginal String: Python 3.9")
    print(f"Reversed String: {reverse_word('Python 3.9')}")
    
    print("\nOriginal String: !olleh")
    print(f"Reversed String: {reverse_word('!olleh')}")