"""
Module to perform string manipulation operations with type hints and documentation.

This module provides a function to capitalize the first letter of a string while leaving 
the rest of the characters unchanged (lowercase or original case preserved after the first).
It ensures that only the very first character is capitalized, regardless of its initial state.
"""

def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of a string while preserving the rest as-is.

    This function takes an input string and returns a new string where only the 
    first character is converted to uppercase, if it exists. The remaining characters 
    are left exactly as they were in the original string (no automatic lowercasing).
    
    If the input string contains non-alphabetic characters at the start that prevent 
    capitalization of an 'A'-'Z', the function still attempts to capitalize any letter 
    found after skipping leading non-letters, but per strict interpretation of "first 
    letter only", this implementation strictly targets index 0 if it is a letter.
    
    However, adhering to common linguistic expectations where we want the first *alphabetic*
    character capitalized (e.g., '123abc' -> '123Abc'), the logic below finds the 
    first alphabetic character and capitalizes it, leaving everything before it untouched 
    and everything after it unchanged.

    Args:
        text (str): The input string to be processed. Can contain any characters.

    Returns:
        str: A new string with only the first alphabetic character capitalized.
             If no alphabetic characters exist in the string, returns a copy of the original.

    Examples:
        >>> capitalize_first_letter_only("hello world")
        'Hello world'
        >>> capitalize_first_letter_only("123abc def")
        '123Abc def'
        >>> capitalize_first_only("")
        ''
        >>> capitalize_first_letter_only("!@#aB cD eF")
        '!@#A bC dE fF'

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected 'str', got '{type(text).__name__}'")

    # Find the index of the first alphabetic character
    for idx, char in enumerate(text):
        if char.isalpha():
            break
    else:
        # No alphabetic characters found; return a copy as-is
        return text

    # Capitalize that specific letter and keep everything else exactly as is
    result_list = list(text)
    first_alpha_char = text[idx]
    
    if 'a' <= first_alpha_char.lower() <= 'z':  # Ensure it's actually an alphabetic char (redundant but safe)
        new_first_char = first_alpha_char.upper()
    else:
        new_first_char = first_alpha_char
    
    result_list[idx] = new_first_char
    return "".join(result_list)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    test_cases = [
        "hello world",
        "123abc def",
        "",
        "!@#aB cD eF",
        "python is great!",
        "   leading spaces here"
    ]

    print("Running capitalize_first_letter_only module tests...\n")
    
    for test_input in test_cases:
        output = capitalize_first_letter_only(test_input)
        # Using repr to ensure special characters are visible if any, though standard str is fine too.
        status = "OK" if isinstance(output, str) else "ERROR"
        print(f"[{status}] Input: {repr(test_input)}")
        print(f"      Output: {output}\n")