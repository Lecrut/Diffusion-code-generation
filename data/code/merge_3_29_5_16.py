def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
        
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1) auxiliary space, excluding output storage.
    """
    result = []
    
    # Iterate from the last character to the first
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
        
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    test_cases = [
        "hello",
        "",
        "a",
        "1234567890",
        "Python is great!",
        "Noob"
    ]

    for original in test_cases:
        reversed_str = reverse_string_iterative(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_str}"\n')