def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string using slicing,
    which is an efficient O(n) operation in Python implemented in C.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string containing characters from the original string 
             in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    samples = [
        "hello world",
        "Python programming is fun!",
        "",
        "a" * 100,
        "Race car"
    ]

    print("Reversed strings:")
    for original in samples:
        reversed_str = reverse_string(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_str}"\n')