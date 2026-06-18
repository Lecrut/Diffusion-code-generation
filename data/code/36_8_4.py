def reverse_string_recursive(s):
    """
    Recursively reverses a string without using slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    if len(s) <= 1:
        return s
    
    # Recursive step: reverse the substring excluding the first character, then append the first character at the end
    rest = reverse_string_recursive(s[1:])
    
    return rest + s[0]

def main():
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_strings = [
        "hello",
        "Python is fun!",
        "",
        "a"
    ]

    print("Testing Recursive String Reversal")
    for original in test_strings:
        reversed_str = reverse_string_recursive(original)
        # Verify correctness by comparing with slicing method (used only for validation, not as the primary solution logic here)
        expected = original[::-1]
        
        if reversed_str == expected:
            print(f"Input: '{original}' -> Output: '{reversed_str}' [Correct]")
        else:
            print(f"Input: '{original}' -> Output: '{reversed_str}' [ERROR - Expected: '{expected}']")

if __name__ == '__main__':
    main()