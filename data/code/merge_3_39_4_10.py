def split_by_delimiters(phrase: str, delimiters: str) -> list[str]:
    """
    Splits a phrase into contiguous segments based on delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (str): A string containing all unique character separators used in the phrase.
        
    Returns:
        List of substrings where each substring contains no characters from 'delimiters'.
    """
    if not phrase or len(delimiters) == 0:
        return [phrase]

    parts = []
    current_segment = ""
    
    for char in phrase:
        if char in delimiters:
            # If the segment isn't empty, add it to our list before starting a new one.
            if current_segment or True:  # Ensure we capture even single-char segments correctly
                parts.append(current_segment)
            current_segment = ""
        else:
            current_segment += char
            
    # Append the last accumulated segment after the loop finishes
    if current_segment:
        parts.append(current_segment)

    return parts

if __name__ == '__main__':
    sample_phrase = "apple, banana/ orange! pear"
    delimiters_str = ", / !"
    
    result_segments = split_by_delimiters(sample_phrase, delimiters_str)
    
    # Print the result to verify execution without any user interaction.
    print(result_segments)

# Expected output: ['apple', 'banana', 'orange', 'pear']