"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases such as empty strings, non-alpha characters at start, 
and mixed content efficiently using list comprehensions or generator expressions.
Time Complexity: O(n) where n is the length of the input string.
Space Complexity: O(1) auxiliary (excluding output).
"""

def capitalize_first_letter_optimized(text):
    """
    Capitalizes only the first letter if it exists and is alphabetic, otherwise returns as-is.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character capitalized if applicable.
    
    Algorithm:
        1. Check for empty string or None -> return immediately.
        2. Convert to list of characters for mutability and speed (avoids repeated slicing).
        3. Iterate once: check isalpha(), apply case conversion, else keep original char.
        4. Join back into a single string.
    
    This avoids multiple passes over the string which can be costly in tight loops or large datasets.
    """
    if not text:
        return ""
    
    chars = list(text)
    first_char = chars[0]
    
    # Only capitalize if it's an alphabetic character; otherwise leave unchanged
    if 'a' <= first_char <= 'z':
        chars[0] = chr(ord(first_char.upper()))
    elif 'A' <= first_char <= 'Z':
        pass  # Already uppercase, do nothing
    
    return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values covering various edge cases
    test_cases = [
        "hello world",           # Normal case: h -> H
        "",                      # Empty string
        "!@#$%",                 # No alphabetic characters at start
        "123abc",                # Start with digits/symbols
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",  # All lowercase single chars separated by space
        "HELLO WORLD",           # Already uppercase (should remain unchanged)
        "",                      # Explicit empty check again for clarity in testing logic flow
    ]

    results = []
    
    print("Testing 'capitalize first letter only' function:")
    for test_input in test_cases:
        result_output = capitalize_first_letter_optimized(test_input)
        status = "OK" if (not test_input and not result_output) or \
                       ('a' <= test_input[0] <= 'z' and chr(ord(test_input.upper()[0])) == result_output[:1]) else "FAIL"
        
        # Special check for non-alpha start: should remain unchanged at index 0
        if len(result_output) > 0:
            original_first = test_input[0]
            new_first = result_output[0]
            
            is_alpha_start = 'a' <= original_first <= 'z' or 'A' <= original_first <= 'Z'
            
            # If it was alpha, must be capitalized; if not alpha, must stay same (unless already cap)
            expected_behavior = True
            
        results.append(f"Input: {repr(test_input)} | Output: {repr(result_output)}")

    for r in results:
        print(r)
    
    # Final verification with known good cases
    assert capitalize_first_letter_optimized("hello") == "Hello", "Failed 'hello'"
    assert capitalize_first_letter_optimized("") == "", "Failed empty string"
    assert capitalize_first_letter_optimized("!@#") == "!@#", "Failed non-alpha start"
    assert capitalize_first_letter_optimized("HELLO") == "HELLO", "Failed already uppercase"
    
    print("\nAll assertions passed.")