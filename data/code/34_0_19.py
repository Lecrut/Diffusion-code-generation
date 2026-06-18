def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters within those words.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return text
    
    # Split into words based on whitespace while preserving original spacing structure is tricky 
    # but standard "capitalize" usually implies splitting by space and joining back.
    # We will split by any whitespace sequence to handle multiple spaces correctly if needed,
    # then rejoin with a single space for clean output as per typical expectations of this task.
    
    words = text.split()
    
    capitalized_words = []
    for word in words:
        if not word:
            continue
        # Capitalize first char, keep rest exactly as is (lowercase or uppercase)
        # Note: str.capitalize() converts the rest to lowercase which violates "preserving the rest of the casing".
        # So we manually handle it.
        new_word = ""
        if word and len(word) > 0:
            first_char = chr(ord(word[0]) + (ord('A') - ord('a')) if 'a' <= word[0] <= 'z' else word[0])
            # Actually, we just want to capitalize the first letter regardless of its current case.
            # The requirement says "capitalizes only the first letter... preserving the rest".
            # This implies: If input is "hElLo", output should be "HeLlO" (only H changed).
            
            if 'a' <= word[0] <= 'z':
                new_word = chr(ord(word[0]) - 32) + word[1:]
            else:
                # If it's already uppercase, leave it. 
                # Wait, "capitalizes" usually means ensure it is upper case A-Z.
                # So if input is 'a', make it 'A'. If input is 'B', keep it 'B'.
                new_word = word[0] + word[1:]
        
        capitalized_words.append(new_word)
    
    return " ".join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file I/O is required.
    samples = [
        "hello world",
        "Python Is Awesome",
        "  multiple   spaces  here ",
        "no change needed",
        "ALL LOWERCASE",
        "MiXeD CaSe"
    ]

    for sample in samples:
        result = capitalize_words(sample)
        print(f'Input: "{sample}" -> Output: "{result}"')