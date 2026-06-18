def capitalize_words(text: str) -> str:
    """
    Capitalize only the first letter of each word in a string.
    
    This function uses list comprehension to create new words with their 
    first character capitalized and then joins them back into a single string.
    It avoids manual indexing loops for better readability and efficiency.
    
    Args:
        text (str): The input string containing multiple words.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    if not isinstance(text, str):
        return ""

    # Split into words, capitalize first char, then join back
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python is awesome",
        "the quick brown fox jumps over the lazy dog",
        "   multiple spaces between words  ",
        "single"
    ]

    for test_input in sample_strings:
        print(f'Input: "{test_input}"')
        result = capitalize_words(test_input)
        print(f'Output: "{result}"\n')