def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    result = []
    for char in s:
        result.insert(0, char)
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = ["hello", "Python3"]
    
    for test_str in sample_strings:
        reversed_str = reverse_string_iterative(test_str)
        print(f"Original: {test_str}")
        print(f"Reversed: {reversed_str}\n")