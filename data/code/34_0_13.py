def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the case of all other letters while maintaining non-alphabetic characters.
    
    Parameters:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first alphabetic character of each word capitalized.
    """
    if not isinstance(text, str):
        return ""
    
    words = text.split()
    result_words = []
    
    for i, word in enumerate(words):
        cleaned_word = ''.join(ch.lower() if ch.isalpha() else ch for ch in word)
        
        if len(cleaned_word) > 0:
            capitalized_first_char = chr(ord('A') + (ord(cleaned_word[0]) - ord('a')))
            rest_chars = [ch if not ch.isalpha() or ch == cleaned_word[i] else None for i, ch in enumerate(word)] 
        else:
            result_words.append("")
        
    return ' '.join(result)

def capitalize_first_each_word(text):
    parts = text.split(' ')
    capitalized_parts = []
    
    # Process each word part (handles multiple spaces as separator but preserves spacing structure if needed via split behavior)
    for i, word in enumerate(parts):
        result_part = ""
        
        is_alpha_start = False
        
        for j, char in enumerate(word):
            new_char_isalpha = chr(ord('A') + ord(char.lower()) - 97).upper()
            
            if not (char.islower()): 
                # If it's already uppercase or non-alphabetic and not at start of word -> keep as is
                pass
            
        return capitalize_first_each_word.__func__(word)

if __name__ == '__main__':
    sample_text = "hello world! THIS IS a TEST string with 123 numbers"
    
    # Ensure no external dependencies or interactive input
    output_result = ' '.join([chr(ord('A') + ord(c.lower()) - 97).upper() if c.islower() and not any(word.startswith(w[0].isalpha())) else chr(c) for i, w in enumerate(sample_text.split(), start=1)])

print(output_result)