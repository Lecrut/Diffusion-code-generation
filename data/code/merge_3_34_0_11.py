def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters within those words.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized.
    """
    if not isinstance(text, str):
        return ""

    # Split into words based on whitespace while preserving original spacing structure implicitly via join
    # We iterate through characters to manually handle title case logic without relying solely on built-in methods 
    # that might alter non-ascii or specific edge cases differently than requested (though Python's default is usually fine).
    # However, the requirement says "capitalizes only the first letter of each word".
    # Standard approach: split by whitespace, capitalize title case per part? No, standard .title() does this.
    # But let's implement robustly to ensure exact behavior requested without external dependencies or side effects.
    
    result = []
    in_word = False
    
    for char in text:
        if not (char.isalpha()):
            # Non-alphabetic characters act as word separators but don't start a new capitalized letter unless they are part of the next alphabetic sequence? 
            # Actually, standard definition: "first letter of each word". Words usually consist of alphanumeric sequences.
            # If we encounter non-alpha (like punctuation), it doesn't get capitalized and breaks the flow if not handled carefully.
            # Let's assume a 'word' starts after whitespace or at index 0.
            
            # Re-evaluating: The prompt says "capitalizes only the first letter of each word".
            # Example: "hello world" -> "Hello World", "hElLo wOrld" (mixed) -> "HElLo WOrld"? 
            # Or does it mean capitalize the *first* char, leave rest as is? Yes. "rest of the casing preserved".
            
            if not in_word:
                result.append(char.lower() if char.isalpha() else char) # Wait, we need to preserve case of first letter too? No, "capitalizes" implies making it uppercase.
                # But wait, what if input is 'hElLo'? First letter should be 'H'. Rest 'ElLo' preserved.
                
            in_word = True
            
        elif char.isalpha():
            if not in_word:
                result.append(char.upper())
                in_word = False
                
    return "".join(result)

# Robust implementation using split and join is more efficient for Python strings than manual iteration 
# unless we need to preserve exact spacing which isn't explicitly requested but "string manipulation" implies efficiency.
# Let's use the standard library approach optimized: capitalize() on words joined back with original separators? 
# No, simpler: replace non-alphabetic chars temporarily if needed? 
# Actually, Python's string methods are highly optimized in C.

def robust_capitalize(text):
    # Split by whitespace to get tokens (words)
    parts = text.split()
    
    capitalized_parts = []
    for part in parts:
        # Capitalize first char of the word, keep rest as is? 
        # Python's str.capitalize() makes first upper and rest lower. We want first upper, rest original case.
        if not part:
            continue
            
        new_part = ""
        first_char = part[0]
        remaining_chars = part[1:]
        
        if first_char.isalpha():
            # If it's already a letter, ensure uppercase (capitalization)
            new_part += first_char.upper()
            
            # Append the rest exactly as they are in original string? 
            # "preserving the rest of the casing" -> Yes.
            # But what if input is '123abc'? Is 1 a word start? Usually words imply alphabetic sequences or tokens separated by space.
            # Let's assume standard English definition: sequence of letters.
            
            # However, to be safe and robust for any "word" (alphanumeric):
            new_part += "".join(char if char.isalpha() else '' for char in remaining_chars) 
            # Wait, this logic is getting complex.
            
        return ""

    # Let's restart with the most efficient standard Pythonic way that fits requirements perfectly:
    # 1. Split into words (sequences of non-whitespace).
    # 2. For each word, take first char and make it upper if alpha? Or just always upper? 
    # "capitalizes" usually implies making uppercase regardless of original case.
    
    pass

# Final efficient implementation logic:
def final_solution(text):
    words = text.split()
    res_words = []
    for w in words:
        if not w: continue
        c1, rest = w[0], w[1:]
        # Capitalize first char (ensure upper)
        cap_c1 = c1.upper()
        # Keep rest exactly as is? 
        # If input is "hElLo", result should be "HElLo".
        # If input is "hello world", result "Hello World".
        
        res_words.append(cap_c1 + rest)
    return ' '.join(res_words)

# Wait, the prompt says "preserving the rest of the casing". 
# Does it mean preserve case relative to original word? Yes.
# So if input is "hElLo", output "HElLo".
# If input has punctuation like "hello-world", is "-" part of word or separator?
# Usually split() handles whitespace only. Punctuation attached to words counts as part of the word in Python's default split().
# Example: "a-b" -> ["a-b"]. First char 'a' becomes 'A'. Rest "-b". Result "A-b". This seems correct interpretation.

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    samples = [
        "hello world",
        "hElLo wOrld",
        "  multiple   spaces ",
        "no change here!",
        "123abc def456"
    ]

    for s in samples:
        print(f'Input: "{s}" -> Output: "{final_solution(s)}"')