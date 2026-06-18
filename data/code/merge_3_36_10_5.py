def reverse_string(s):
    """
    Reverses a given string using slicing, which is Pythonic and efficient.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or external dependencies
    test_strings = ["Hello, World!", "Python", "A man a plan a canal Panama"]
    
    print("Original String Reversal Examples:")
    print("-" * 30)
    
    for original in test_strings:
        reversed_str = reverse_string(original)
        print(f"Original: {original}")
        print(f"Reversed:{reversed_str}\n")