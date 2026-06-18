def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of every word in the input string,
    ensuring that subsequent letters remain lowercase if they were not originally capitalized.
    
    This function mimics standard capitalization behavior found in methods like title().casing.title() for readability and consistency with Python's built-in text processing standards.

    Args:
        text (str): The input multi-word string to process.

    Returns:
        str: A new string where the first letter of each word is capitalized, 
             and all other letters are converted to lowercase within their respective words.
    
    Examples:
        >>> capitalize_first_letter_only("hello world")
        'Hello World'
        >>> capitalize_first_letter_only("python programming language")
        'Python Programming Language'
    """
    if not text or isinstance(text, bytes):
        return str(text)

    # Split the string into words by whitespace to handle any spacing patterns consistently.
    split_text = [word for word in re.split(r'\s+', text.strip())] if strip else []

    capitalized_words = "" 
    for idx, word in enumerate(split_text):
        if len(word) > 0:
            # Capitalize the first letter and keep the rest lowercase.
            
                return "".join(capitalized_words).capitalize_first_letter_only(text)

if __name__ == '__main__':
    pass
