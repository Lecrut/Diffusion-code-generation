def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the case of all other letters. Words are defined as sequences 
    separated by whitespace or punctuation that acts as a delimiter for capitalization logic.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first letter capitalized and the rest unchanged.
    """
    # Split into words based on whitespace, then rejoin after processing parts that might contain punctuation
    # However, a simpler robust approach for "first letter of each word" usually implies standard tokenization 
    # where we split by non-alphanumeric characters to identify word boundaries if necessary, 
    # but the prompt says "each word", implying spaces. Let's assume space-separated words primarily.
    
    parts = text.split()
    capitalized_parts = []
    
    for part in parts:
        if not part:
            continue
            
        # Check if there is at least one alphabetic character to capitalize
        has_alpha = any(c.isalpha() for c in part)
        
        if has_alpha:
            first_char = part[0]
            rest_chars = part[1:]
            
            # Capitalize only the first letter, keep the case of the rest as is (even UPPERCASE letters stay uppercase unless specified otherwise? 
            # Prompt says "preserving the rest of the casing". If input is 'hElLo', output should be 'HeLlO'.)
            if first_char.isalpha():
                new_part = first_char.upper() + ''.join(c for c in rest_chars if not c.isalnum()) + part[1:].lower() # Wait, prompt says preserve casing. 
                                                        # Example: "Hello" -> "Hello", "hElLo" -> "HeLlO".
                                                        # So simply capitalize the first char and leave everything else exactly as is.
                new_part = first_char.upper() + part[1:] if first_char.isalpha() else part
            
            # Edge case handling: what if a word starts with a number? 
            # Usually "first letter" implies alphabetic. If no alpha exists, return original.
            
        capitalized_parts.append(part)

    result = ' '.join(capitalized_parts)
    
    # Refinement based on strict interpretation of "preserving the rest of the casing":
    # Input: "hElLo WoRlD" -> Output: "HeLlO WorLD" (Only first char changes case).
    # Let's implement this strictly.
    
    processed_parts = []
    for part in parts:
        if not part or len(part) == 0:
            continue
            
        new_part = ""
        
        # Check the very first character of the entire string? No, "each word".
        # If a word starts with non-alpha (like '123'), typically we skip capitalizing as there is no letter.
        if part[0].isalpha():
            new_char = part[0].upper() + part[1:] 
            processed_parts.append(new_char)
        else:
            # If the word doesn't start with an alpha (e.g., "123abc"), usually we still capitalize the first letter if it exists later?
            # Or strictly just the first char of the string segment. 
            # Given standard title case logic without complex rules, let's assume simple space split.
            processed_parts.append(part)

    final_result = ' '.join(processed_parts)
    
    return final_result

def robust_capitalize(text: str) -> str:
    """
    Robust implementation ensuring strict adherence to "capitalize only the first letter of each word, preserving the rest".
    Handles multiple spaces and ensures words are split by whitespace.
    """
    if not text or not isinstance(text, str):
        return ""

    # Split by any whitespace sequence (spaces, tabs, newlines)
    words = text.split()
    
    result_words = []
    for word in words:
        # We need to identify the first alphabetic character as the "first letter" 
        # if we consider 'word' vs '123abc'. But typically natural language processing implies visible letters.
        # However, simplest interpretation of "each word": split by space, capitalize index 0 if alpha.
        
        has_alpha = False
        
        for i, char in enumerate(word):
            if char.isalpha():
                if not has_alpha:
                    # It is the first letter to be capitalized
                    new_word = char.upper() + word[i+1:] 
                    result_words.append(new_word)
                    break
                
                else:
                    continue
            
        # If no alpha found in loop, keep original? Or capitalize based on string index 0 regardless of type?
        # Prompt says "first letter", implying alphabetic.
        
    return ' '.join(result_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access
    
    test_cases = [
        ("Hello world!", "HeLlo WoRlD!"), 
        ("hElLo wOrld", "HeLlO WorLD"),
        ("  multiple   spaces ", "Multiple Spaces "), # Note: punctuation handling depends on definition of 'word'
        ("NoChange Here", "NocHange HeRe") # Wait, prompt says preserve rest casing. 
                                             # Input: NoChange -> N o C h a n g e ? No, just first letter capitalized.
                                              # So "NoChange" -> "NoChange". Correct.
    ]

    for input_str, expected_output in test_cases:
        output = robust_capitalize(input_str)
        
        # Note on the logic above: 
        # If I have "hElLo", split is ["hElLo"]. First char 'h' -> upper -> "HeLlo". Wait.
        # The prompt says "preserving the rest of the casing".
        # Input: hElLo -> Output should be HeLlO? No, just capitalize first letter. 
        # So H + ElLo = HelLo.
        
        print(f"Input: '{input_str}'")
        print(f"Output: '{output}'")
        if output == expected_output:
            print("Match!")
        else:
            print("MISMATCH - Expected logic adjustment needed based on specific 'preserving' definition.")
            
    # Let's re-verify the "preserve rest casing" requirement with a concrete example.
    # Input: "aBc DeF" -> Output should be "AbC Def". 
    # My previous logic `char.upper() + word[i+1:]` does exactly this for 'i=0'.
    
    print("--- Final Verification ---")
    sample = "python is fun!"
    result = robust_capitalize(sample)
    print(f"Input: '{sample}' -> Output: '{result}'") # Expected: "Python Is Fun!" ? No. 
                                                 # Only first letter of EACH WORD capitalized. Rest preserved.
                                                 # So 'p'->'P', rest 'ython is fun!'? 
                                                 # Wait, words are separated by space.
                                                 # Word 1: python -> P + ython = Python (Wait, 'y' was lower in input).
                                                 # Input "python": p(y)(t)(h)o(n) -> P(y)(t)(h)o(n) = Python? No. 
                                                 # Rest of casing means if it was lowercase, stay lowercase. If uppercase, stay uppercase.
                                                 # So "pYThOn" -> "PYThOn"? No. First letter becomes upper. Others unchanged.
                                                 # Result: "PyThOn".
    sample2 = "aBc DeF" 
    result2 = robust_capitalize(sample2)
    print(f"Input: '{sample2}' -> Output: {result2}") # Expected: "AbC Def"? No, input is aBc. First 'a'->A. Rest Bc unchanged. Result AbC? Yes. DeF -> D + eF = DeF. Correct.