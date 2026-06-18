def analyze_string_characters(text: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.
    
    Args:
        text (str): The input string to be analyzed.
        
    Returns:
        A tuple containing:
            - set(str): A set of all unique characters in the string.
            - list(str): A list of characters that appear more than once, 
                         preserving the order of their first occurrence as a repeated char.
    """
    if not text:
        return set(), []

    seen = {}
    duplicates = []
    
    # First pass to identify unique chars and track repetition without modifying original string for duplicate detection logic clarity
    # We'll iterate through the string once, tracking count or presence
    
    char_count = {}
    repeated_chars_set = set()
    
    for char in text:
        if char not in seen:
            seen[char] = True
        
        # Check duplication

if __name__ == '__main__':
    pass
