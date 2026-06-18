import unicodedata

def case_swap(text: str) -> dict:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' to their respective
    case transformations of the input string. Prioritizes readability and performance.

    Args:
        text (str): The input string to transform.

    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    lower_text = text.lower()
    upper_text = text.upper()
    
    # Construct title case by iterating only once, which is more performant for long strings
    if not lower_text:
        title_text = ""
    else:
        words = lower_text.split(' ')
        title_words = []
        capitalize_next = True

if __name__ == '__main__':
    pass
