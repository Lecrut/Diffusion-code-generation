def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to count occurrences of each letter that is repeated.
    
    Args:
        s (str): The input string containing letters and potentially other characters.
        
    Returns:
        dict[str, int]: A dictionary where keys are the repeated letters 
                        and values are their occurrence counts in the original string.
                        Only includes letters with a count > 1.
    
    Note:
        - Case-sensitive comparison is used (e.g., 'A' != 'a').
        - Non-letter characters are ignored during counting but do not affect logic.
        - If no letter is repeated, an empty dictionary is returned.
    """
    # Dictionary to store counts of each character found in the string
    char_counts = {}

    # Iterate through each character in the input string
    for char in s:
        if char.isalpha():  # Only consider alphabetic characters
            # Increment count for this character
            char_counts[char] = char_counts.get(char, 0) + 1

    # Filter to only include characters that appear more than once
    repeated_letters = {char: count for char, count in char_counts.items() if count > 1}

    return repeated_letters

if __name__ == '__main__':
    sample_string = "hello world"
    
    result_dict = process_string(sample_string)
    
    print(f"Input string: '{sample_string}'")
    print("Dictionary of repeated letters and their counts:")
    for letter, count in result_dict.items():
        print(f"{letter}: {count}")

    # Additional test case to ensure robustness with mixed case
    sample_string2 = "AaBaBc"
    
    result_dict2 = process_string(sample_string2)
    
    print("\nInput string: '" + sample_string2 + "'")
    print("Dictionary of repeated letters and their counts:")
    for letter, count in result_dict2.items():
        print(f"{letter}: {count}")