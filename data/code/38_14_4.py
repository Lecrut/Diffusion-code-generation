def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find repeated letters and their counts.
    
    Only lowercase alphabetic characters that appear more than once are included in the result.
    Non-alphabetic characters (like spaces or punctuation) are ignored for counting purposes but 
    do not affect which letters are considered 'repeated'. The comparison is case-insensitive,
    so 'A' and 'a' count as the same letter if both appear multiple times.

    Args:
        s (str): Input string to process.

    Returns:
        dict[str, int]: Dictionary with keys being repeated letters (lowercase) 
                        and values being their occurrence counts in the original string.
    """
    # Normalize input to lowercase for case-insensitive processing
    normalized_s = s.lower()
    
    letter_counts = {}
    
    # Count occurrences of each alphabetic character
    for char in normalized_s:
        if 'a' <= char <= 'z':  # Ensure only letters are counted
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Filter to keep only repeated letters (count > 1) and return as dictionary
    result = {letter: count for letter, count in letter_counts.items() if count > 1}
    
    return result

if __name__ == '__main__':
    sample_string = "Hello World! This is a test case with repeated letters."
    output_dict = process_string(sample_string)
    print(output_dict)