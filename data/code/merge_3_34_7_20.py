import re

def capitalize_words(text: str) -> str:
    """
    Decorator-like function that automatically capitalizes the first letter 
    of every word in a given string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split the string into words based on whitespace and punctuation boundaries
    # Using regex to find sequences of alphabetic characters as "words"
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return text
    
    capitalized_words = []
    for word in words:
        # Capitalize the first letter and keep the rest lowercase (standard title case behavior per word)
        # However, to strictly follow "capitalize the first letter", we just cap the first char.
        if len(word) > 0:
            capitalized_word = word[0].upper() + word[1:]
        else:
            capitalized_word = ""
        capitalized_words.append(capitalized_word)

    # Reconstruct the string preserving original non-word characters roughly by joining words back with spaces
    # A simpler approach for general usage is to use str.title(), but let's implement logic manually 
    # to ensure we only touch alphabetic parts if needed, or just return title() behavior.
    
    # Actually, Python's built-in .title() does exactly this: capitalizes the first character of each word.
    # To avoid over-engineering and potential edge cases with non-letters while keeping it simple:
    result = text.title()
    
    return result

# Example usage demonstrating functionality
if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is a test string for the decorator",
        "python programming language",
        "no words here!",
        ""
    ]

    print("Input -> Output")
    print("-" * 30)
    
    for s in sample_strings:
        output = capitalize_words(s)
        print(f"'{s}' => '{output}'")