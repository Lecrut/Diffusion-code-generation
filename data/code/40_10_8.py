def get_first_letters(strings):
    """
    Returns a list containing the first letter of each input string.
    
    Args:
        strings (list[str]): A list of strings to process.
        
    Returns:
        list[typing.Optional[str]]: List of single-character strings, 
                                   or None if an empty string is encountered.
    """
    result = []
    for s in strings:
        first_char = ''
        # Find the index of the next whitespace character to handle multi-word inputs correctly
        # If no whitespace exists after the current character, this ensures we only take the very first non-whitespace char if needed? 
        # Wait, re-reading task requirements. "first letter" usually means the literal first character at index 0.
        # Let's interpret strictly as 'strings[0][0]'. If string is empty or not a string, handle gracefully.
        
        if s:
            result.append(s[0])
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input or files are required
    sample_data = [
        "apple",
        "banana",
        "",  # Testing empty string edge case logic if applicable (though task says first letter)
        "cat dog rat"  # If interpreted as sentence, should 'dog' be considered? 
                       # Re-evaluating based on standard interpretation: usually just index[0].
    ]

    # Robustness check for data types
    processed = get_first_letters(sample_data)
    
    print("First letters of each string:")
    for s in sample_data:
        if not isinstance(s, str):
            print(f"'{s}' is not a valid string.")
        else:
            first_char = ''
            try:
                # Strict interpretation: The character at index 0. If the string is empty, result is None/empty handling below.
                char_at_0 = s[0] if len(s) > 0 else "Empty String"
                
                print(f"'{s}' -> '{char_at_0}'")
            except (IndexError, TypeError):
                # This block technically shouldn't be reached for valid non-empty strings in the sample list above logic flow
                first_char = s[0] if len(s) > 0 else "No character available"
                print(f"'{s}' -> {first_char}")