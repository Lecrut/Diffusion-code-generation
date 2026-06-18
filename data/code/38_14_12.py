def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find letters that appear more than once.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        dict: A dictionary where keys are repeated letters 
              and values are their occurrence counts in the original string.
              
    Note: Only alphabetic characters are considered, case-insensitive matching is applied.
          If a letter appears exactly once or zero times (after filtering non-alphabets), it won't be included.
    """
    # Dictionary to store frequency of each character
    char_counts = {}
    
    # Iterate over the string and count occurrences
    for char in s:
        if char.isalpha():  # Only consider alphabetic characters
            lower_char = char.lower()
            char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    
    # Filter to only include letters that are repeated (count > 1)
    result = {char: count for char, count in char_counts.items() if count > 1}
    
    return result

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string with repeated characters like 'a', 'e', and 's'."
    
    # Process the hard-coded sample value
    output_dict = process_string(sample_string)
    
    # Output the result as requested (dictionary format printed directly)
    print(output_dict)