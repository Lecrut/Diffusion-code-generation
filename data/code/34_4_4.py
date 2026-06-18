import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             preserving original casing for subsequent characters and non-alphabetic prefixes.
    """
    if not isinstance(text, str):
        return ""

    words = text.split()
    result_words = []

    for word in words:
        # Check if there is at least one alphabetic character to capitalize
        has_alpha = False
        capitalized_word_list = list(word)
        
        for i, char in enumerate(capitalized_word_list):
            if 'a' <= char.lower() <= 'z':
                has_alpha = True
                
                # Capitalize the first letter of the word only once per alphabetic character found at start
                # However, standard behavior usually means capitalize the very first letter 
                # and leave others as is unless they are also letters.
                # The prompt says "capitalizing only the first letter". 
                # Interpretation: First char if alpha -> upper; rest unchanged? 
                # Or does it mean title case but strictly one per word?
                # Let's assume standard Title Case behavior where we capitalize the first alphabetic char of each word.
                
                capitalized_word_list[i] = char.upper()
        
        result_words.append("".join(capitalized_word_list))

    return " ".join(result_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, arguments, or network access is required.
    samples = [
        "hello world",
        "python programming language",
        "the quick brown fox jumps over the lazy dog",
        "no change here"
    ]

    for text in samples:
        output = capitalize_first_letter(text)
        print(f"{text} -> {output}")