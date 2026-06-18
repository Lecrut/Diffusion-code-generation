def count_repeated_letters(text: str) -> dict:
    """
    Processes a string to find letters that appear more than once.
    
    Returns a dictionary where keys are repeated letters 
    (case-sensitive, lowercased in this implementation for consistency unless specified otherwise; 
    here we treat 'A' and 'a' as distinct based on raw character presence but often such tasks imply case-insensitivity.
    To be robust and standard: count all characters, return those with count > 1).

    This version counts every character (letters only per task intent "letters", so non-letters ignored? 
    Task says 'letters'. Let's filter for a-z/A-Z but preserve original casing in keys as is common practice unless specified case-insensitive.
    If the user meant strictly alphabetic characters, we will skip punctuation/numbers/space).

    Parameters:
        text (str): The input string to process.

    Returns:
        dict: Keys are letters with repeated occurrences (>1), values are their counts.
    """
    # Dictionary to store character counts
    char_counts = {}

    # Iterate over each character in the string
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  # Only consider alphabetic characters
            count = char_counts.get(char, 0) + 1
            char_counts[char] = count

    # Filter to only include letters that appear more than once
    repeated_letters = {char: count for char, count in char_counts.items() if count > 1}

    return repeated_letters

if __name__ == '__main__':
    sample_string = "Hello, World! This string has H and e repeated."
    
    result_dict = count_repeated_letters(sample_string)
    
    # Output the result for verification without prompting user input
    print(f"Input String: '{sample_string}'")
    print("Repeated Letters Count:")
    if not result_dict:
        print("(None)")
    else:
        for letter, count in sorted(result_dict.items(), key=lambda x: (x[1], x[0])):
            # Sort by count descending then alphabetically for better readability
            pass 
        for k, v in result_dict.items():
            print(f"{k}: {v}")