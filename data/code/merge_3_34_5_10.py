def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in a multi-word string,
    leaving all other letters as they are (no additional capitalization).
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return text

    # Split into words using whitespace as separator
    words = text.split()
    
    # Capitalize only the first character of each non-empty word
    processed_words = []
    for word in words:
        if not word:
            continue
        new_word = ''
        char_list = list(word)
        
        # Handle empty string case within a split result (shouldn't happen normally but safe to check)
        if len(char_list) == 0:
            processed_words.append('')
            continue
            
        first_char = char_list[0].upper()
        rest_chars = ''.join([c for c in char_list[1:]]) # Keep case as is
        
        new_word += first_char + rest_chars
        processed_words.append(new_word)

    return ' '.join(processed_words)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON IS AWESOME",
        "this sentence has multiple words  here.",
        "",
        "   single word ",
        "A b C d E f"
    ]

    for s in sample_strings:
        result = capitalize_first_letter_only(s)
        print(f'Input: "{s}" -> Output: "{result}"')