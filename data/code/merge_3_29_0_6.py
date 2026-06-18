"""
Script to reverse a given input string efficiently.
Handles edge cases such as empty strings and various character sets (unicode, symbols, etc.).
No external libraries or interactive prompts are used.
"""

def reverse_string(input_str: str) -> str:
    """
    Reverses the provided input string in-place conceptually by slicing.
    
    Args:
        input_str (str): The string to be reversed. Can contain any character set including unicode and symbols.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    # Python's slice notation [::-1] efficiently handles all characters, spaces, special chars, emojis, etc.
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction or external files.
    test_cases = [
        "Hello World",           # Standard string with space and capitalization
        "",                      # Edge case: Empty string
        "!@#$%^&*()",            # String with special symbols
        "Emoji 🚀🌍✨",          # Unicode characters including emojis
        "12345 67890 !_",       # Mixed alphanumeric and punctuation
    ]

    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        print(f"Original: '{test_input}'")
        print("Reversed: '{reversed_result}'\n".format(reversed_result=reversed_result))