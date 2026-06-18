"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases: empty strings, non-letter start chars (keeps original char), 
multiple letters in sequence (only capitalizes the very first).
Time Complexity: O(n) where n is the length of the input string.
Space Complexity: O(1) if modifying in-place via list conversion, or O(n) for immutable strings.

The solution prioritizes speed by avoiding unnecessary function calls and 
minimizing object creation during iteration over common use cases (e.g., large text).
"""

def capitalize_first_optimized(text):
    """
    Capitalize only the first letter of the string if it is alphabetic.
    
    Rules:
    1. If the string is empty, return as-is.
    2. Identify the index of the first alphabetic character found scanning left-to-right.
       - Optimization: Stop immediately after finding a valid target to capitalize 
         (though we must process up to that point for slicing).
    3. If no alphabetic character is found, return as-is.
    4. Replace only that specific letter with its uppercase equivalent; leave the rest unchanged.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with first alphabet capitalized.
        
    Examples:
        >>> capitalize_first_optimized("hello") -> "Hello"
        >>> capitalize_first_optimized("") -> ""
        >>> capitalize_first_optimized("123abc!") -> "123Abc!"
        >>> capitalize_first_optimized("!@#$%") -> "!@#$%"
    """
    
    # Handle empty string immediately to avoid index errors and save computation
    if not text:
        return ""
    
    n = len(text)
    
    # Find the first alphabetic character's index for optimization logic
    idx_to_capitalize = 0
    
    # Linear scan until we find an alphanumeric that isn't a digit 
    # (we specifically look for letters to capitalize, but preserve digits/punctuation as is).
    # Actually, standard 'capitalize' behavior in many contexts implies finding the first letter.
    # Let's define: Find first char that is 'a'-'z' or 'A'-'Z'.
    
    found_alpha_idx = -1
    
    for i in range(n):
        c = text[i]
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            # If it's already uppercase, we don't strictly need to "change" case 
            # but usually the task implies ensuring it is upper. 
            # However, looking at edge cases like "123Abc", if 1 is first non-alpha? 
            # Let's stick to: Capitalize the FIRST LETTER OF THE STRING IF IT IS A LETTER.
            found_alpha_idx = i
            break
            
    # If no letter exists in the string (e.g., "!@#$%") or it starts with a digit/other,
    # per strict interpretation of "capitalize first letter only" where there is NO letter: return as is.
    if found_alpha_idx == -1:
        return text
        
    # Extract parts before and after the target character for efficient slicing 
    # (avoiding string concatenation overhead in a loop, though simple join is usually fast enough)
    
    prefix = text[:found_alpha_idx]
    char_to_capitalize = text[found_alpha_idx]
    suffix = text[found_alpha_idx + 1:]
    
    # Convert to uppercase only if it's not already (optional optimization check could go here, 
    # but simple upper() is C-optimized) and proceed.
    capitalized_char = char_to_capitalize.upper()
    
    return prefix + capitalized_char + suffix

if __name__ == '__main':
    # Hard-coded sample values to test edge cases without external input
    samples = [
        "hello world",           # Normal case -> Hello world
        "",                      # Empty string
        "!@#$%",                 # No letters, punctuation only -> !@#$% (no change) or handle logic? 
                                # Based on spec: capitalize first LETTER. If no letter, nothing to cap.
        "123abc",               # Starts with digit -> 123Abc ? Or leave as is? 
                               # Re-reading task: "capitalize the first letter". 
                               # If there is a 'b' later, it's not the FIRST letter of the string.
                               # It implies capitalize text[0] if text[0].isalpha().
        "!Hello",               # Starts with symbol -> !Hello (unchanged) or Hello?
                               # Usually "capitalize first word" vs "first character". 
                               # Task says: "capitalize the first letter ONLY".
                               # This implies: Find the first alphabetic char and capitalize IT.
                               # Example "!abc" -> "!Abc"? Or is it just text[0]?
                               # Let's assume standard behavior: Capitalize if alphanumeric start?
                               # Most robust interpretation for "first LETTER": 
                               # Scan from left, find first letter, capitalize THAT specific one.
        None                     # Null check (though type hint says str)
    ]

    test_results = []
    
    for s in samples:
        try:
            if s is None: continue
            
            result = capitalize_first_optimized(s)
            
            # Debugging print logic to show input/output pairs clearly without extra text outside code block scope effectively? 
            # The prompt asks for a runnable module, so prints are fine.
            test_results.append((s, result))
        except Exception as e:
            test_results.append(f"Error with {repr(s)}: {e}")

    if not any(isinstance(x[0], str) and x != "Error..." for x in test_results): 
       # Fallback check just to ensure we ran at least one string case cleanly above.
       
        pass
        
    print("Input -> Output")
    print("-" * 40)
    
    # Display results based on our logic interpretation:
    # Case 1: "hello world" -> 'Hello' + rest? Or just capitalize first char if alpha? 
    # If I interpret "capitalize the first letter only" as modifying ONLY that one character to upper case.
    # Then "hello world" becomes "Hell o world"? NO, usually it means capitalizing the start of the word/string contextually or literally.
    # Given "first letter", literal interpretation: 
    # If text[0] is alpha -> Upper(text[0]) + rest.
    # Else if there's a later alpha? The prompt says "the first LETTER". 
    # It does NOT say "capitalize the string starting with...".
    # So for "!abc", first letter is 'a' (index 1). Result: "!Abc"? 
    # Wait, standard python str.capitalize() makes it start with upper. 
    # But task says "first letter ONLY" and explicitly mentions edge cases like punctuation.
    # This strongly suggests scanning to find the first alphabetic character and capitalizing THAT one specifically.
    
    for inp, out in test_results:
        print(f"{repr(inp):20} -> {repr(out)}")

if __name__ == '__main__':
    pass
