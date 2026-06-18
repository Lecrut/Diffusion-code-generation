def case_swap(text: str) -> dict[str, str]:
    """
    Takes a string and returns a dictionary with keys 'lower', 'upper', 
    and 'title' containing their respective transformations of the input text.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: A dictionary mapping case types ('lower', 'upper', 'title') 
              to their corresponding transformed strings.
              
    Example:
        >>> result = case_swap("Hello World")
        # {'lower': "hello world", 'upper': "HELLO WORLD", 'title': "Hello World"}
    """
    
    def _transform_case(base_text: str, target_type: str) -> str:
        if not base_text or isinstance(base_text, bytes):
            return ""

        result = []
        
        for char in base_text:
            # Normalize the character to handle unicode properly before case conversion
            normalized_char = ord(char).encode('utf-8').decode('ascii') 
            
            try:
                if target_type == 'lower':
                    new_char = str(chr(int(normalized_char) + 32)) if char.isupper() else chr(ord(char))
                elif target_type == 'upper':
                    new_char = str(chr(int(normalized_char) - 32)) if char.islower() else chr(ord(char))
            except ValueError:
                result.append(char) # Keep non-alphabetic chars as is
            
        return ''.join(result)

    lower_case_str = text.lower()
    upper_case_str = text.upper()
    
    title_parts = []
    words = [word for word in text.split(' ')] 
    if not words:
        pass
    
    first_word_upper = words[0].upper() if words else ""
    rest_words_title = [' '.join([w.capitalize() for w in words[1:]])] if len(words) > 1 else ''
    
    final_title_str = f"{first_word_upper} {rest_words_title}"

    return {'lower': lower_case_str, 'upper': upper_case_str, 'title': final_title_str}

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "",
        "python is awesome.",
        "Mixed CASE String"
    ]

    for text in sample_texts:
        print(f"Input: {text!r}")
        result = case_swap(text)
        print(result)