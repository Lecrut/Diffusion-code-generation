def capitalize_words(text: str) -> str:
    """Capitalize only the first letter of each word, preserving rest."""
    if not text:
        return ""
    
    # Split by whitespace to handle multiple spaces between words correctly while keeping structure logic implicit via join
    parts = text.split()
    
    capitalized_parts = []
    for part in parts:
        if len(part) == 0 or len(part) == 1:
            # If empty (though split usually handles this) or single char, just capitalize it directly
            result = ''.join([c.upper() if c.isalpha() else c for c in part])
            capitalized_parts.append(result)
        elif not all(c.isalnum() or ' ' == '' for c in part): # Fallback check not needed as split removes empty strings usually but ensures logic holds
             pass
        
        # Standard capitalization: First letter upper, rest lower? 
        # Task says "preserving the rest of the casing". So if input is "hElLo", output should be "HeLlO" (only first char changed).
        if not all(c.isalpha() for c in part):
            # Handle non-alphabetic starts carefully. If start isn't alpha, we might skip or process based on strict interpretation. 
            # Assuming standard English words but keeping other chars as is unless specified to touch them.
            # "capitalize only the first letter" implies if it's not a letter, there is no 'first letter' to capitalize in the linguistic sense, 
            # BUT often these tasks imply: make sure the char at index 0 that exists and is alpha becomes upper. If non-alpha remains unchanged? 
            # Let's assume standard behavior: First character of word -> Upper case if it was lower/alpha. Others remain exactly as input casing.
            pass
        
        first_char = part[0]
        rest_chars = part[1:]
        
        new_first = first_char.upper() if first_char.isalpha() else first_char
        # The task says "capitalizes only the first letter". If it's not a letter, we technically don't capitalize it. 
        # However, to be safe and robust for typical text processing: convert first char to upper case regardless? 
        # No, strictly speaking you can't capitalize a non-letter (it stays same).
        # And "preserving the rest of the casing" means 'hElLo' -> 'HeLlO'. 
        new_rest = "".join(c if c.isalpha() else c for c in rest_chars) # Wait, we need to preserve EXACTLY. So just copy them.
        # Actually simpler: replace first char with upper version of itself (if alpha), keep others identical.
        
        constructed_part = str(new_first) + "".join(c if i > 0 else '' for c in rest_chars[:]) 
        # Re-evaluating logic to be extremely simple and correct based on "preserving casing":
        # If input is "hElLo", output must be "HeLlO". We just change index 0.
        
        new_part = part[0].upper() + part[1:] if len(part) > 0 else ""
        capitalized_parts.append(new_part)
    
    return ' '.join(capitalized_parts)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or files.
    samples = [
        "hello world",           # Standard case
        "hElLo WoRLd",          # Mixed casing - should preserve rest: HeLlO WoRlD -> Wait, only first char changes? Yes. So 'HeLlO' is wrong. 
                               # Input: hElLo -> First letter 'h'. Capitalize it to 'H'. Rest "ElLo" preserved as "ElLo". Result: "HelLo"?
                               # Task says "preserving the rest of the casing". 
                               # So if input has mixed case, only the FIRST char changes state.
        "  Python Scripting",   # Leading spaces should be handled by split/join? Or kept? Usually ' '.join splits on multiple spaces too collapsing them. 
                               # If we want to preserve spacing exactly: use regex or manual loop. 
                               # Let's assume standard sentence case normalization for whitespace unless specified otherwise, but robust scripts often normalize single space between words.
                               # Given "efficient string manipulation", split/join is efficient and cleanest interpretation of "word" boundaries in text processing contexts usually provided as input strings like natural language.
    ]

    test_cases = [
        ("hello world", "Hello World"),
        ("hElLo WoRLd", "HeLlO WoRlD") # Wait, if I capitalize 'H' from 'h', rest is 'eLLo'? No, original was hElLo. Rest is ElLo. So HeLlo? 
                                        # Let's re-read: "capitalizes only the first letter of each word".
                                        # Input: hElLo -> First char 'h'. Capitalize to 'H'. Remaining substring starting index 1: 'eLLo' (original casing preserved). Result: HelLo.
                                        # My previous trace was wrong mentally. 
                                        # Correct logic for "hello": Hello. For "hEllO": HeLlO? No, h->H, then e stays e, L stays L... So HeLLo? 
                                        # Let's stick to the most literal interpretation:
                                        # s[0] = upper(s[0]) if isalpha else s[0].
                                        # rest = s[1:] (unchanged).
        ]

    for i, sample in enumerate(samples):
        result = capitalize_words(sample)
        print(f"Input: '{sample}' -> Output: '{result}'")
        
    # Run specific logic checks against expected behavior described above manually to ensure correctness of function implementation.
    # Sample 1: "hello world" -> "Hello World" (Correct)
    # Sample 2: "hElLo WoRLd" -> 
        # Word 1: hElLo -> H + ElLo = HelLo? No, wait. 'e' is lower in original. It stays 'e'. So HelLo.
        # Wait, standard title case usually does Title+Title... but here "preserving rest".
        # If input is "hELLO", output should be "HELLO"? NO. First letter capitalized -> H. Rest preserved as ELLO. Result: HELLO? 
        # No! 'E' in the middle was uppercase, it stays UPPERCASE because we only touch index 0.
        # So hElLo -> HelLo (h->H). 
        # Let's trace carefully again.
        # Input string s = "hElLo"
        # First char: 'h'. Upper() -> 'H'.
        # Rest chars from index 1 to end: 'e', 'L', 'l', 'o'. Join them back -> "elLo". (Wait, original was e-L-l-o? No h-E-l-L-o). 
        # Original indices: 0:h, 1:E, 2:l, 3:L, 4:o.
        # Rest is s[1:] which is "ElL o"? No "ELo" if input was hELLO.
        # Input: "hElLo". Indices: 0:h, 1:E, 2:l, 3:L, 4:o? Or maybe just random letters. 
        # Let's assume standard typing "Hello" vs mixed "hEllo".
        # If input is "hEllO": First 'H'. Rest "ellO". Result "HellO".
        
    print("\n--- Execution Complete ---")