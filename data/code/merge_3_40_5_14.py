def get_first_letters(text: str) -> dict[str, str]:
    """
    Takes a string and returns a dictionary where keys are words 
    and values are their respective first letters (lowercase).
    
    Punctuation is ignored when determining the first letter.
    Words are defined as sequences of alphanumeric characters separated by non-alphanumeric characters.

    Args:
        text (str): The input string to process.

    Returns:
        dict[str, str]: A dictionary mapping each word to its lowercase first letter.
    """
    words = []
    
    # Split the text into potential tokens based on whitespace and punctuation
    # We'll manually iterate to handle mixed alphanumeric/punctuation correctly
    current_word_chars = []
    
    for char in text:
        if char.isalnum():
            current_word_chars.append(char)
        else:
            if len(current_word_chars) > 0:
                words.append("".join(current_word_chars))
                current_word_chars = []
    
    # Add the last word if exists (in case string doesn't end with punctuation/whitespace)
    if len(current_word_chars) > 0:
        words.append("".join(current_word_chars))

    result_dict = {}
    
    for word in words:
        first_char = word[0].lower()
        
        # Only add to dictionary if the key is not already present 
        # (to handle duplicate words, though typically keys are unique per requirement interpretation)
        # If duplicates should be allowed as separate entries or overwritten?
        # Standard dict behavior overwrites. The prompt implies "keys are the words", so one entry per word type.
        
        if first_char not in result_dict:
            result_dict[first_char] = word

    return result_dict

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    
    # Hard-coded sample values as requested (using the variable for clarity but ensuring no input prompts)
    output_result = get_first_letters(sample_text)
    
    print(f"Input: {sample_text}")
    print("Output Dictionary:")
    for key in sorted(output_result.keys()):
        print(f"{key}: '{output_result[key]}'")