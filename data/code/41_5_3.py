def case_converter(s):
    """
    Takes a string and returns three variations: lowercase, uppercase, 
    and title-cased versions using manual loops and conditionals.
    
    Args:
        s (str): The input string to convert.
        
    Returns:
        tuple: A tuple containing (lowercase_string, uppercase_string, title_case_string)
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Initialize result strings
    lower_result = ""
    upper_result = ""
    title_result = ""

    for char in s:
        is_alpha = 'a' <= char <= 'z' or 'A' <= char <= 'Z'
        
        if not is_alpha:
            # Non-alphabetic characters remain unchanged across all cases
            lower_result += char
            upper_result += char
            title_result += char
        else:
            # Determine case based on character value
            ord_val = ord(char)
            
            # Lowercase conversion logic
            if 'A' <= char <= 'Z':
                lower_result += chr(ord_val + 32)
            else:
                lower_result += char
            
            # Uppercase conversion logic
            if 'a' <= char <= 'z':
                upper_result += chr(ord_val - 32)
            else:
                upper_result += char
                
            # Title case logic (uppercase first letter of word, lowercase rest)
            # For simplicity in this manual implementation without tracking words,
            # we will apply title casing by converting the current character 
            # to uppercase if it's alphabetic and not already handled as part of a sequence.
            # However, true "title case" requires knowing word boundaries.
            # Since the prompt asks for conditional logic manipulation per char:
            # We'll implement a simple version where we capitalize every letter 
            # that follows a non-letter or is at the start (simplified to just capitalizing first of string and lowercasing rest? 
            # No, standard title case means cap first letter of each word. 
            # Without explicit word boundary tracking in one pass without state for previous char type:
            # Let's assume simple logic: Capitalize if it's the start or after a space/punctuation.
            
            prev_char = ""  # We can't easily access previous char in pure loop without storing, but we can store last added
            
            # To do true title case manually per character requires knowing context (previous char).
            # Let's restructure slightly to track if current is start of word or just apply standard rule:
            # Capitalize first letter, lowercase the rest? No, that's not full title case.
            
            # Revised approach for Title Case within this constraint:
            # We'll assume words are separated by spaces and simple punctuation.
            # But to keep it strictly per-character conditional as requested without complex state machine overkill:
            # We will capitalize the character if it is alphabetic AND (it's at index 0 OR previous char was not alpha/space).
            
            pass

    # Re-implementing title case logic correctly with a single loop by tracking context
    lower_result = ""
    upper_result = ""
    title_result = ""
    
    prev_is_alpha_or_space = False
    
    for i, char in enumerate(s):
        is_alpha = 'a' <= char <= 'z' or 'A' <= char <= 'Z'
        
        if not is_alpha:
            lower_result += char
            upper_result += char
            title_result += char
            prev_is_alpha_or_space = False # Reset flag for next word start? Actually, space starts a new word.
            continue
            
        # Determine case based on position in "word" (simplified by assuming words are sequences of letters)
        is_start_of_word = not prev_is_alpha_or_space
        
        if 'A' <= char <= 'Z':
            lower_result += chr(ord_val + 32)
            
            upper_result += char
            
            # Title case: Capitalize first letter, lowercase subsequent ones in word
            if is_start_of_word:
                title_result += char
            else:
                title_result += chr(ord(char.lower()))
                
        elif 'a' <= char <= 'z':
            lower_result += char
            
            upper_result += chr(ord_val - 32)
            
            # Title case logic for lowercase chars in word
            if is_start_of_word:
                title_result += char.upper()
            else:
                title_result += char

        prev_is_alpha_or_space = True

    return lower_result, upper_result, title_result

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    samples = [
        "Hello World",
        "Python Programming 2024!",
        "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    ]

    print("Case Converter Results")
    for sample in samples:
        lower, upper, title = case_converter(sample)
        print(f"\nInput: '{sample}'")
        print(f"Lowercase: '{lower}'")
        print(f"Uppercase: '{upper}'")
        print(f"Title Case: '{title}'")