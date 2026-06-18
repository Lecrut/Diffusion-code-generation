def reverse_string(s: str) -> str:
    """
    Reverses a given string using Python's built-in slicing, 
    which is efficient (O(n)) and idiomatic.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction or external dependencies used.
    test_cases = [
        "Hello, World!",
        "",
        "Python is awesome",
        "A man a plan a canal Panama"
    ]

    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f"Original: {original}")
        print(f"Reversed: {reversed_str}\n")