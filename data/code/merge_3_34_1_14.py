def capitalize_first_letter_only(text: str) -> str:
    """
    Returns a new string where only the first character of every word is capitalized.
    
    This function handles multiple spaces between words by preserving them, ensuring that 
    we do not accidentally merge or lose spacing information from the original input.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return ""

    result = []
    
    # Track whether we are currently inside a word (i.e., after non-space characters)
    in_word = False
    
    for char in text:
        if char.isspace():
            # If there was an active word, close it and reset the flag
            if in_word:
                result.append(char)
                in_word = False
            else:
                result.append(char)
        elif not in_word:
            # Start of a new word -> capitalize first letter
            if char.isalpha():
                result.append(char.upper())
                in_word = True
            else:
                # Non-alphabetic character at start (e.g., punctuation): keep as is, don't treat as "first letter" yet? 
                # However, standard definition of 'word' usually implies alphabetic sequence.
                # If the char isn't alpha but we are starting a word-like structure:
                result.append(char)
                in_word = True  # Consider it part of the start until an alpha comes or end
        else:
            # Inside a word -> lowercase if alphabet, keep otherwise? 
            # The requirement says "only first char... capitalized". Implies rest should be lowercased.
            result.append(char.lower())

    return "".join(result)

if __name__ == '__main__':
    samples = [
        "hello world",
        "  multiple   spaces ",
        "python is awesome!",
        "",
        "no change here",
        "UPPERCASE mixed case"
    ]

    for s in samples:
        print(f'Input : "{s}"')
        print(f'Output: "{capitalize_first_letter_only(s)}"\n')