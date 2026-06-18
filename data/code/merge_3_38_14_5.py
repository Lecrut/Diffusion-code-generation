def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to count occurrences of each letter that is repeated.
    
    Args:
        s (str): The input string containing letters and potentially other characters.
        
    Returns:
        dict[str, int]: A dictionary where keys are the repeated letters 
                        (case-sensitive) and values are their occurrence counts.
    """
    # Dictionary to store letter counts for only those with count > 1
    result = {}

    # Iterate over each character in the string
    for char in s:
        if 'a' <= char.lower() <= 'z':  # Check if it's a lowercase or uppercase English letter
            current_count = result.get(char, 0) + 1
            
            # Only update count if this is not already tracked as repeated (to avoid double counting logic issues in loop)
            # However, since we are iterating and building counts on the fly for all chars first mentally:
            pass

    # Re-approach with a cleaner two-pass or single-dict accumulation approach
    char_counts = {}
    
    # First pass: count total occurrences of each letter (case-sensitive as per standard string processing unless specified otherwise)
    for char in s:
        if 'a' <= char.lower() <= 'z':  # Ensure we only process alphabetic characters
            char_counts[char] = char_counts.get(char, 0) + 1

    # Second pass: filter to keep only letters that appear more than once
    repeated_letters_dict = {letter: count for letter, count in char_counts.items() if count > 1}
    
    return repeated_letters_dict

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    sample_string = "hello world"
    
    output_dictionary = process_string(sample_string)
    
    print(output_dictionary)

# Expected Output: {'l': 3, 'o': 2} 
# Explanation: In "hello world": h(1), e(1), l(3), o(2), w(1), r(1), d(1). Only 'l' and 'o' are repeated.