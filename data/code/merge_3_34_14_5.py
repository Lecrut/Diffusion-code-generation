"""Module to capitalize the first letter of each word in a string."""

def title_case(text: str) -> str:
    """Capitalize only the first letter of each word in the given text.
    
    Args:
        text (str): The input string containing words separated by whitespace.
        
    Returns:
        str: A new string with the first letter of each word capitalized,
             preserving original spacing and casing for remaining letters.
             
    Example:
        >>> title_case("hello world")
        'Hello World'
    """
    return " ".join(word.capitalize() if len(word) > 0 else "" 
                    for word in text.split())

if __name__ == '__main__':
    sample_text = "the quick brown fox jumps over the lazy dog"
    result = title_case(sample_text)
    print(result)