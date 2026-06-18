def reverse_string(s: str) -> str:
    """
    Reverses a given string iteratively in O(n) time complexity without using built-in reversal methods.
    
    Parameters:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    result = []
    # Iterate from the last character to the first
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    reversed_result = reverse_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Reversed: {reversed_result}")