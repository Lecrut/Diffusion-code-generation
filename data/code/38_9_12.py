def analyze_string_characters(text: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        tuple: A tuple containing two elements:
            - set[str]: A set of all unique characters in the string.
            - list[str]: A list of characters that appear more than once, 
                        preserving their order of first appearance.
    
    Example:
        >>> analyze_string_characters("hello")
        ({'h', 'e', 'l', 'o'}, ['l'])
    """
    if not text:
        return set(), []

    # Track counts and maintain order for repeated characters
    char_counts = {}
    seen_order = []  # To preserve the first occurrence of each character
    
    unique_chars_set = set()
    
    for char in text:
        unique_chars_set.add(char)
        
        if char not in char_counts:
            char_counts[char] = 0
        
        char_counts[char] += 1

        # If this is the second time we see a character, add it to our repeated list.
        # We only want each repeated character once in the result list.
        if char_counts[char] == 2:
            seen_order.append(char)

    return unique_chars_set, seen_order

if __name__ == '__main__':
    sample_text = "programming"
    
    unique_characters, repeated_characters = analyze_string_characters(sample_text)
    
    print(f"Input string: '{sample_text}'")
    print(f"Unique characters (set): {unique_characters}")
    print(f"Repeated characters (list): {repeated_characters}")