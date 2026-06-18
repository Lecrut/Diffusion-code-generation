def analyze_string_characters(text: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.

    Args:
        text (str): The input string to analyze.

    Returns:
        tuple[set[str], list[str]]: A tuple containing:
            - set[str]: Unique characters found in the string.
            - list[str]: Characters that appear more than once, preserving order of first appearance.
    """
    unique_chars = set()
    repeated_chars = []

    for char in text:
        if char not in unique_chars:
            unique_chars.add(char)
            # Check if this character has been seen before (already added to list but maybe missed logic?)
            # Actually, we need a separate count or check against the 'seen' set vs just adding once.
            pass
        
        # Correct approach for repeated detection based on frequency > 1:
        # We can do two passes or one pass with counting. Let's use a simple counter dict for clarity and efficiency.

    from collections import Counter
    
    char_counts = Counter(text)
    
    unique_set = set(char_counts.keys())
    repeated_list = [char for char, count in char_counts.items() if count > 1]
    
    return (unique_set, repeated_list)

if __name__ == '__main__':
    sample_text = "hello world"
    result_tuple = analyze_string_characters(sample_text)
    unique_chars, repeated_chars = result_tuple
    
    print(f"Unique characters: {sorted(unique_chars)}")
    print(f"Repeated characters (in order of appearance): {repeated_chars}")