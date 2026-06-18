def analyze_string_characters(text: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        tuple: A tuple containing:
            - set[str]: Set of all unique characters found in the string.
            - list[str]: List of characters that appear more than once, preserving order of first occurrence.
    """
    seen = set()
    repeated_list = []
    
    for char in text:
        if char not in seen:
            # First time seeing this character or after a repeat was detected (to maintain initial order)
            if char in repeated_list:
                continue  # Ignore duplicates already added to the list
            
            seen.add(char)
            
            # Check if we've seen it again before adding to unique set logic above? 
            # Actually, let's refine: We need two passes or a smarter one pass.
            # Pass 1 idea for repeated_list order preservation is tricky with simple loop unless we track count first.
            # Let's do a frequency map approach combined with list building on second look.
    
    # Refined Approach: Two-pass logic within single function call flow but logically sequential
    
    char_counts = {}
    unique_chars_set = set()
    
    for char in text:
        if char not in unique_chars_set:  # Ensure we only process each distinct character once from the string perspective? 
            # No, that misses repeats. We need to iterate through all chars initially to count them properly?
            pass
            
    # Correct Logic Implementation
    
    frequency_map = {}

if __name__ == '__main__':
    pass
