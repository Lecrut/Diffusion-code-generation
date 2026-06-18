"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases: empty strings, non-alphabetic start characters, 
and ensures only the very first character is capitalized if it's alphabetic.
Time Complexity: O(n) where n is the length of the input string (single pass).
Space Complexity: O(1) auxiliary space excluding output storage.

Usage Example:
    >>> solve("hello world") -> "Hello world"
    >>> solve("") -> ""
    >>> solve("!@#$%") -> "!@#$%"
    >>> solve("  python3 ") -> "  Python3 "
"""

def capitalize_first_letter(s: str) -> str:
    """
    Capitalizes the first alphabetic character of the string if it exists.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter capitalized, 
             preserving all other characters exactly as they were in the original.
             
    Logic:
    - If the string is empty or None, return it unchanged.
    - Iterate through the string until an alphabetic character is found at index 0.
    - If such a character exists, capitalize it and join back with the rest of the characters.
    - Otherwise (if no letter starts the string), return original to preserve non-alphabetic start behavior 
      consistent with "only first letter" instruction interpretation for edge cases like "!hello".
    
    Note: This implementation avoids creating intermediate lists or slicing repeatedly in loops,
          instead using a single pass and efficient string concatenation via join on necessary parts.
    """
    if not s:
        return s
    
    # Find the index of the first alphabetic character
    idx = None
    for i, char in enumerate(s):
        if char.isalpha():
            idx = i
            break
            
    # If no letter found at all or before any other chars (e.g., "!@#"), return as is.
    # The task says "capitalize the first letter", implying we only act on letters.
    # Edge case: string starts with non-letter -> do nothing to maintain integrity of input structure.
    if idx is None:
        return s
    
    # Construct result by capitalizing char at idx and keeping prefix/suffix intact
    prefix = s[:idx]  # Characters before the first letter (could be empty or punctuation)
    suffix = s[idx+1:]  # Everything after that character
    
    if len(prefix) == 0:
        return f"{s[0].upper()}{suffix}"
    
    # If there are non-letter chars before, we still capitalize only the first letter found.
    # But wait - "capitalize the first letter" usually implies position-based or value-based?
    # Given edge cases like punctuation at start: 
    # Interpretation A: Capitalize s[0] if it's a letter -> "!hello" -> "!Hello"? No, that changes meaning.
    # Interpretation B (more common in such tasks): Find first alphabetic char and capitalize IT only.
    # Example: "  hello world" -> "  Hello world", "!@#hello" -> "!@#Hello".
    
    return f"{prefix}{s[idx].upper()}{suffix}"

if __name__ == '__main':
    # Hard-coded sample values to test functionality without user input or external dependencies.
    samples = [
        "hello world",           # Standard case: capitalizes 'h' -> "Hello"
        "",                      # Empty string edge case
        "!@#$%",                 # No letters at all
        "  python3 ",            # Leading/trailing spaces, internal numbers preserved
        "a1b2c3",                # Starts with letter immediately
        "!!!abc",                # Punctuation before first actual letter 'a' -> should become "!!lbc"? 
                                 # Wait: logic above finds idx=0 for '!'? No, ! is not alpha.
                                 # So idx will be 4 ('a'). Result: "!@#Abc" if input was "!!!abc".
                                 # Let's trace manually with code logic:
                                 # Input: "!!!abc", loop skips indices 0,1,2 (non-alpha), finds 'a' at 3.
                                 # prefix = s[:3] -> "!!!"
                                 # suffix = s[4:] -> "bc"
                                 # result = "!!!" + "A" + "bc" -> "!l!Abc"? No: !@@@ A bc? 
                                 # Actually input string is "!!!abc", so prefix="!!!", char='a', upper='A', suffix="bc".
                                 # Output: "!l!Abc" was typo in thought, correct output is "!!!Abc".
        None,                    # Test with None (though type hint says str, runtime handles gracefully)
    ]

    results = []
    for test_input in samples:
        try:
            res = capitalize_first_letter(test_input if isinstance(test_input, str) else "")
            results.append((test_input, res))
        except Exception as e:
            results.append((f"Error processing {repr(test_input)}", f"{e}"))

    # Print results in a clean format for verification.
    print("Input -> Output")
    print("-" * 40)
    for inp, out in results:
        if isinstance(inp, str):
            print(f"'{inp}' -> '{out}'")
        else:
            print(f"{repr(inp)} -> {repr(out)}")

if __name__ == '__main__':
    pass
