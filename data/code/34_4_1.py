import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             while preserving case for all other characters and whitespace structure.
    """
    words = text.split()
    result_words = []
    
    for word in words:
        if not word:  # Handle empty strings or multiple spaces resulting from split
            continue
        
        first_char = word[0]
        rest_chars = word[1:]
        
        capitalized_word = ""
        
        if len(first_char) == 1 and (first_char.isalpha() or ord(' ') <= ord(first_char) < ' '.encode()[0]): # Check for non-whitespace character at start of word
            try:
                first_uppercase = chr(ord(first_char) - 32) if not first_char.isupper() else first_char
                capitalized_word += first_uppercase + rest_chars[1:] if len(rest_chars) > 0 else "" # Handle single char words correctly by slicing carefully
                
                # Re-evaluate logic for simplicity and correctness without complex unicode assumptions on ord values directly in this context.
                
                # Correct approach:
                new_first = word[0].upper() if not (word[0] == ' ') or len(word) > 1 else word[0] 
                rest_of_word = word[1:]
                capitalized_words.append(new_first + ''.join([c.lower() for c in rest_of_word])) # Wait, task says capitalize ONLY first letter. Do NOT lowercase others unless specified? "capitalizing only the first letter" usually implies standard Title Case where subsequent letters remain as is or are lowercased? 
                
                # Re-reading: "capitalizing only the first letter of each word".
                # Interpretation A: First char upper, rest unchanged (e.g., "hello world" -> "Hello World").
                # Interpretation B: Standard title case (First char upper, rest lower) e.g. ("hElLo WoRLd" -> "HeLlO WoRld"? No, usually means standardizing). 
                
                # Most common interpretation for this phrasing is A: First letter uppercase, everything else stays exactly as it was in the original word (except spaces removed if split happened).
                # However, often users expect Title Case behavior. Let's stick to strict literal meaning unless "standard" implies otherwise.
                # Literal: "a b C d e" -> "A B c D E". 
                
                capitalized_word = first_uppercase + rest_chars
                
            except Exception as e:
                print(f"Error processing word {word}: {e}", file=sys.stderr)
        else:
             pass
            
    return ' '.join(result_words if result_words else [])

# Refined Logic for Capitalize First Letter Only (Literal Interpretation):
def capitalize_first_letter_v2(text: str) -> str:
    """
    Returns the text with only the first character of each word capitalized.
    All other characters remain unchanged from the original input.
    """
    words = text.split()
    
    if not words:
        return ""

    result_words = []
    
    for i, word in enumerate(words):
        # Ensure we don't process empty strings (though split usually handles this)
        if len(word) == 0:
            continue
            
        first_char = word[0]
        
        # Check if the character is a letter to capitalize it properly. 
        # If it's not an alpha, just keep as is? Or force upper? Usually implies letters only.
        try:
            if 'a' <= first_char <= 'z':
                capitalized_first = chr(ord(first_char) - 32)
            elif 'A' <= first_char <= 'Z':
                capitalized_first = first_char
            else:
                # If it's not a letter, we can't capitalize in the traditional sense. 
                # We'll just keep it as is to avoid breaking non-text input like numbers/symbols if that was intended, 
                # but typically "first letter" implies alphabetic.
                capitalized_first = first_char
        except Exception:
            capitalized_first = word[0]

        rest_of_word = word[1:]
        
        result_words.append(capitalized_first + ''.join(rest_of_word))
    
    return ' '.join(result_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    samples = [
        "hello world",
        "python is great!",
        "  multiple   spaces ",
        "A B C D E"
    ]

    for sample in samples:
        print(f"Input: '{sample}'")
        output = capitalize_first_letter_v2(sample)
        print(f"Output: '{output}'")