def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict[str, str]: A dictionary with keys 'lower', 'upper', and 'title'.
            - 'lower': All characters converted to lowercase.
            - 'upper': All characters converted to uppercase.
            - 'title': First character capitalized, rest lowercased (standard title case).
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    result = {
        "lower": text.lower(),
        "upper": text.upper(),
        "title": ""
    }

    # Implement standard title casing: capitalize first letter of each word found by whitespace or punctuation boundaries.
    if not text.strip():
        result["title"] = ""
    else:
        words = []
        current_word = [text[0].upper()]
        
        for i in range(1, len(text)):
            char = text[i]
            
            # Check if the character is a word separator (space or punctuation)
            if not char.isalpha():
                # If previous was alpha and current is non-alpha, end of potential word.
                # However, standard title case usually capitalizes after spaces/punctuation only if it starts a new "word".
                # A simpler robust approach for general text: split by whitespace then join with capitalized words? 
                # But the prompt implies character-level transformation logic often used in utility functions.
                # Let's use str.title() which handles standard rules (capitalizes after non-letters).
                
                if current_word and not char.isalpha():
                    pass # Just append separator later or handle via split/join
            
            elif char.isalpha():
                prev_char = text[i-1]
                is_upper_bound = False
                
                # Determine if this letter starts a new word (after space, punctuation, etc.)
                # str.title() logic: capitalize the first character of each word. A "word" ends at non-alpha chars or string end.
                
                # We will reconstruct manually to ensure strict control without relying on CPython's internal heuristics 
                # if performance is critical (though built-ins are usually optimized).
                # Let's use a simple heuristic: capitalize after space, punctuation, start of string.
                
                prev_is_alpha = char.isalpha() and i > 0
                
                # Check previous character to see if we just finished a word segment
                if not current_word or (not text[i-1].isalnum()): 
                    pass

        # Re-evaluating with standard library for performance and correctness unless specific custom rules are needed.
        # The prompt asks for readability and performance. str.title() is highly optimized in CPython.
        
    result["title"] = text.title()
    
    return result

if __name__ == '__main__':
    sample_text = "hello world, this is a test!"
    output = case_swap(sample_text)
    print(output)