def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
            - 'lower': All characters converted to lowercase.
            - 'upper': All characters converted to uppercase.
            - 'title': First character capitalized, rest lowercased (if applicable).
    
    Performance Note: Uses built-in string methods which are implemented in C 
    for optimal performance and readability.
    """
    text_lower = text.lower()
    text_upper = text.upper()
    
    # Title case logic: capitalize the first word(s) if present, then lower the rest
    # This handles standard title casing rules (e.g., "hello world" -> "Hello World")
    def to_title_case(word):
        return word[0].upper() + word[1:].lower() if len(word) > 0 else ""

    text_parts = text.split(' ')
    parts_mapped = [to_title_case(p) for p in text_parts]
    
    # Reconstruct title case string, preserving original spacing structure roughly 
    # but ensuring proper capitalization of words. For simplicity and standard behavior:
    if len(text_parts) == 0 or all(len(p) <= 1 for p in text_parts):
        text_title = "".join(to_title_case(p))
    else:
        text_title = " ".join(parts_mapped)

    return {
        'lower': text_lower,
        'upper': text_upper,
        'title': text_title
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    samples = [
        "hello world",
        "PYTHON IS FUN!",
        "",
        "a b c d e"
    ]

    for text in samples:
        result = case_swap(text)
        print(f"Input: '{text}'")
        print(f"Lower: {result['lower']}")
        print(f"Upper: {result['upper']}")
        print(f"Title: {result['title']}")
        print("-" * 20)