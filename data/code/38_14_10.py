def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find letters that appear more than once.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary where keys are repeated letters 
                        and values are their occurrence counts in the original string.
                        Only includes characters with count > 1.
    """
    char_count = {}
    
    # Count occurrences of each character (case-sensitive)
    for char in s:
        if char.isalpha():  # Consider only alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    
    # Filter to keep only repeated letters and return as dictionary
    result = {char: count for char, count in char_count.items() if count > 1}
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values - runs without user input or external dependencies
    test_string = "hello world hello"
    
    repeated_letters_dict = process_string(test_string)
    
    print(f"Input string: '{test_string}'")
    print("Repeated letters and their counts:")
    for letter, count in sorted(repeated_letters_dict.items()):
        print(f"{letter}: {count}")