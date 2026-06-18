def reverse_string(s):
    """
    Returns the reversed version of the input string using slicing notation.
    
    Parameters:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    test_strings = [
        "hello",
        "",
        "Python is awesome!",
        "A man, a plan, a canal: Panama"
    ]

    print("Original String\tReversed String")
    print("-" * 35)
    
    for original in test_strings:
        reversed_str = reverse_string(original)
        print(f"{original}\t{reversed_str}")