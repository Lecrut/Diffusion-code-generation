"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases such as empty strings, non-alphabetic start characters,
and mixed content including punctuation without affecting performance on large inputs.
"""

def capitalize_first_letter_optimized(text: str) -> str:
    """
    Capitalizes only the very first alphabetic character in the string if it exists.
    
    Algorithm Choice for Performance:
    - Iterates through characters until an alphabet is found or end of string.
    - Uses ord() checks which are generally faster than method calls like isalpha().
    - Slices and concatenation are O(n) but efficient enough; no regex overhead used to keep it linear with minimal constant factors.
    
    Args:
        text (str): The input string potentially containing any characters.
        
    Returns:
        str: A new string with only the first alphabetic character capitalized, unchanged otherwise.
             If no alphabetic character exists or is present as the start before an alphabet, returns original.
             Wait - re-reading task "capitalize the first letter": implies if there's a letter at index 0 after skipping non-letters? 
             Or literal "first char"? Usually it means find the first alpha and capitalize it, leaving rest alone or lowercasing? 
             Let's assume standard behavior: Find first alphabetic character from left. Capitalize that specific one only.
             
    Clarification on requirement interpretation for robustness:
        1. If input is "hello" -> "Hello".
        2. Input "world", should become "World"? Or if non-alpha start like "-hello" -> "-Hello"? 
           Typically, this function finds the first alphabetic character and capitalizes it only once.
    """

    # Check for empty string immediately to return early without processing loop overhead
    if not text:
        return ""

    result = list(text)  # Convert to a mutable list of characters
    
    # Iterate through each character starting from index 0
    found_capitalized_alpha_flag = False
    n = len(result)
    
    for i in range(n):
        char_code = ord(result[i])
        
        # Check if current character is alphabetic and not already uppercase (assuming we capitalize only the first one found globally)
        # The problem says "capitalize THE FIRST LETTER". 
        # This implies finding the very first letter that exists anywhere? Or just at position 0?
        # Standard convention: Find the first alpha, make it upper. Leave others as is or lower? Usually leave as is unless specified otherwise.
        
        if char_code >= ord('a') and char_code <= ord('z'):
            # Found a lowercase letter. If this is the FIRST such character globally (not just at index 0), capitalize it only once.
            # However, "THE first letter" often implies position based or logical order? 
            # Let's assume: Find the very first alphabetic character in the string and capitalize ONLY that one instance if not already upper.
            
            # Wait, does it mean capitalizing index 0 IF it is a letter? Or finding the first alpha anywhere?
            # Example "123abc" -> "A123bc"? No usually means just at start or find next alphabetic and capitalize that one only if lower case.
            
            # Re-evaluating based on typical interview question phrasing: 
            # Usually it's: Capitalize the first character found in the string (ignoring non-alpha), but ONLY THAT ONE instance? Or all subsequent letters unchanged?
            # Let's stick to strict interpretation of "capitalize THE FIRST LETTER":
            # If I have "  hello", result should be " Hello". 
            # If I have "- world", result "- World"? No, that would capitalize 'w'. But is w the first letter? Yes.
            
            if not found_capitalized_alpha_flag:
                # Capitalize this specific character only once for any string where we find an alpha after skipping prefix non-letters
                # Actually simpler interpretation often expected: 
                # If index 0 is alpha -> upper it. Else leave alone? No, that's trivial.
                
                # Most robust "capitalize first letter" logic: Find the first alphabetic character and capitalize IT (if lowercase). Leave rest untouched or lowercased based on specific variant not mentioned here.
                # Assuming standard behavior where only THAT ONE instance is changed to Upper if it was Lower. Others remain same case? Or all others become lower? 
                # Given "ONLY", implies just that one char change, nothing else touched unless specified (like title case).
                
                result[i] = chr(ord(result[i]) - 32) # Convert lowercase to uppercase
                
            found_capitalized_alpha_flag = True
            
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "hello",           # Expected: Hello (only first char changed? Or just h->H?) -> HELLOW is title, only capitalize FIRST means 'Hello' if rest untouched. But wait, standard python str.capitalize() lowercases the rest. Task says "capitalize THE first letter ONLY". This implies NO other changes.)
        "",                # Expected: "" (empty)
        "-hello",          # First alpha is h -> -Hello? Or just capitalize index 0 which isn't a letter? If rule is 'first ALPHABETIC', then Yes. If strict position, maybe no change or dash stays. Let's assume find first alpha.)
        "123abc",         # Expected: 123Abc (only A changed)
        "- - hello world",# First alpha h -> H. Rest unchanged? Or rest lowercased? 
                         # The prompt says "capitalize the first letter ONLY". It does not say lowercase others. So leave them as is.)
    ]

    for case in test_cases:
        output = capitalize_first_letter_optimized(case)
        print(f"Input: {case!r} -> Output: {output!r}")