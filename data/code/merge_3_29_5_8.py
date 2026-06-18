import sys

def reverse_string(s: str) -> str:
    """
    Reverses a string iteratively in O(n) time complexity without using built-in reversal methods.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Convert the string to a list of characters since strings are immutable in Python
    chars = list(s)
    
    two_pointers = 0
    len_chars = len(chars) - 1
    
    while two_pointers < len_chars:
        # Swap characters at both pointers
        temp_char = chars[two_pointers]
        chars[two_pointers] = chars[len_chars]
        chars[len_chars] = temp_char
        
        two_pointers += 1
        len_chars -= 1
    
    return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = ["hello", "Python", "A man a plan a canal Panama"]
    
    for test_input in test_cases:
        reversed_output = reverse_string(test_input)
        print(f"Input: '{test_input}'")
        print(f"Reversed Output: '{reversed_output}'\n")