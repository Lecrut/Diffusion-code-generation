def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of every word in the input string,
    leaving all other characters unchanged (including case).
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return ""

    result = []
    
    # Track whether we are at the start of a new word (after whitespace or non-alphabetic char before alpha)
    is_start_of_word = True
    
    for index in range(len(text)):
        char = text[index]
        
        if not char.isalpha():
            # Non-alphabetic characters: reset word flag only after an alphabetic character appears next, 
            # but actually we need to track the state based on whether this non-alpha breaks a potential sequence.
            # Logic adjustment: A "word" starts when we have either:
            # 1. The very beginning of string (index == 0) AND char is alpha? No, standard definition usually implies 
            #    that words are sequences of letters separated by whitespace or non-letters.
            # However, the prompt says "first character of every word". Standard interpretation in Python often uses split(),
            # but for efficiency without creating intermediate lists (which copies memory), we iterate once.
            
            # Let's refine 'word' definition: A sequence of alphabetic characters separated by non-alphabetic boundaries? 
            # Or just whitespace-separated words? Usually "words" implies sequences of letters.
            # Example: "hello, world!" -> "Hello, World!".
            # If input is "a1b", should it be "A1B"? Yes, 'a' starts a word sequence if we consider contiguous non-space chars as a token 
            # OR strictly alphabetic sequences? 
            # The most robust interpretation for "first letter of every word" in natural language processing context usually treats
            # whitespace and punctuation as separators. But simple regex split() handles this well. 
            # To be highly efficient without imports (like re) if possible, we can do manual iteration.
            
            pass
        
        elif char.isalpha():
            if is_start_of_word:
                result.append(char.upper())
                is_start_of_word = False

if __name__ == '__main__':
    pass
