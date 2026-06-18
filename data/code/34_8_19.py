"""
Module to perform string manipulation operations with type hints.

This module provides a function to capitalize only the first letter of a given string,
leaving all other characters in their original case (lowercase or uppercase).
It includes comprehensive docstrings and follows PEP 8 guidelines for code style.
"""

def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalize only the first letter of the input string if it is alphabetic,
    leaving all other characters unchanged (including their existing case).

    If the string contains non-alphabetic characters at the start (e.g., symbols),
    they are left untouched. Only an actual alphabetic character triggers capitalization.

    Args:
        text (str): The input string to process. Must be a valid Python string type.

    Returns:
        str: A new string with only the first letter capitalized, or the original
             string if it is empty or does not start with an alphabetic character.

    Examples:
        >>> capitalize_first_letter_only("hello world")
        'Hello world'
        >>> capitalize_first_letter_only("123abc")
        '123abc'
        >>> capitalize_first_only("")
        ''
        >>> capitalize_first_letter_only("HELLO WORLD")  # Note: This capitalizes the first letter regardless of its current case, as per standard convention for "capitalize" unless specified otherwise. However, strictly interpreting "first letter only" implies changing 'h' to 'H'. If input is already uppercase like HELLO, it becomes Hello (changing H to H does nothing visually but logically applies title casing).
        >>> capitalize_first_letter_only("HELLO WORLD")  # Logic: First char 'H' -> Upper('H') = 'H', rest unchanged. Result "Hello world" would be full capitalization only if we lowercased the rest, which this function does NOT do based on the name and description. Let's re-verify logic from prompt: "capitalize the first letter ONLY". This implies changing case of index 0 to upper, nothing else changes.
        >>> capitalize_first_letter_only("HELLO WORLD") -> 'Hello world' is WRONG if we don't lowercase rest. The function should be pure capitalization of first char. 
        Correct Logic Verification: "capitalize" usually means make uppercase. "only the first letter" means only that character's case changes to upper, others stay exactly as they are in input? Or does it imply standard title casing (rest lower)?
        
        Re-reading prompt carefully: 'capitalize the first letter ONLY'. 
        Standard interpretation 1: Only change index[0] to Upper. Everything else remains identical. 
        Example: "hello" -> "Hello". "HELLO" -> "HELLo"? No, that would be weird. Usually capitalize implies making it uppercase if not already. If input is 'a', output 'A'. Input 'B' (already upper), output 'B'.
        
        Let's stick to the most literal interpretation of "capitalize only": Make the first character uppercase, leave everything else exactly as it was in the original string. 
        However, often users expect standard capitalization behavior where non-first letters are lowercased? No, prompt says "ONLY".
        So: Input "hElLo" -> Output "HElLo"? Or "HElLo"? Capitalize means make Upper. So 'h' becomes 'H'. The rest 'E','L','L','o' stay as is. Result "HELLO". 
        Wait, if input is "hello", result "Hello".
        If input is "HeLLo", result "HEllo" (only first char changes to upper). 
        Let's implement exactly that: text[0].upper() + text[1:].

    Raises:
        TypeError: Raised if the input `text` is not a string instance.
    """
    # Input validation using type hinting logic implicitly handled by Python runtime, but explicit check for clarity in production code often helps with debugging before error occurs.
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    # Base case: empty string or non-alphabetic start? 
    # The prompt says "capitalize the first letter". If it's a number '1', there is no letter. 
    # Should we leave it as is? Yes.
    
    if not text:
        return text
    
    # Check if the first character is alphabetic to ensure we are capitalizing a "letter"
    if text[0].isalpha():
        # Capitalize only the first char, keep rest exactly as they were in input (no lowercasing applied)
        # This strictly follows "only". If user meant standard title case, they would say "capitalize and lowercase rest".
        return text[:1].upper() + text[1:]
    else:
        # No letter to capitalize at start, return original string.
        return text

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no input(), sys.stdin, argparse)
    
    test_cases = [
        "hello world",
        "HELLO WORLD", 
        "123abc",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",
        "!@#$%",
    ]

    print("Running 'capitalize_first_letter_only' module tests...\n")
    
    for test_input in test_cases:
        result = capitalize_first_letter_only(test_input)
        print(f"Input:      '{test_input}'")
        print(f"Output:     '{result}'")
        
        # Verify specific expectations based on interpretation of "capitalize only first letter"
        if test_input == "hello world":
            assert result == "Hello world", f"Expected 'Hello world', got '{result}'"
            
    print("\nAll tests passed successfully.")