def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters. Handles multiple spaces and empty strings gracefully.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first character of each word capitalized.
    """
    if not isinstance(text, str):
        return ""
    
    # Split by whitespace and reconstruct while capitalizing the first letter of non-empty tokens
    words = text.split()
    result_parts = []
    
    for word in words:
        if len(word) > 0:
            capitalized_word = word[0].upper() + word[1:]
            result_parts.append(capitalized_word)
        else:
            # Preserve empty strings from split (though split() without args usually removes them, 
            # keeping logic robust for edge cases if modified later)
            pass
            
    return ' '.join(result_parts)

if __name__ == '__main__':
    sample_inputs = [
        "hello world",
        "python programming is fun!",
        "",
        "   multiple      spaces   here  ",
        "single"
    ]
    
    for test_input in sample_inputs:
        output = capitalize_words(test_input)
        print(f'Input: "{test_input}"')
        print(f'Output: "{output}"\n')