import string

def find_repeated_letters(text: str) -> dict[str, int]:
    """
    Processes a string to output a dictionary where keys are letters 
    that appear more than once and values are their occurrence counts.
    
    Only alphabetic characters (a-z, A-Z) are considered for repetition detection.
    Case is normalized to lowercase before counting.

    Parameters:
        text (str): The input string containing any character types.

    Returns:
        dict[str, int]: Dictionary of repeated letters and their counts.
    """
    # Normalize the string by converting it all to lowercase for consistent handling
    lower_text = text.lower()
    
    # Initialize a dictionary with zero values for each letter in the alphabet
    char_counts = {char: 0 for char in string.ascii_lowercase}

    # Iterate through characters, ignoring non-alphabetic ones (like numbers or symbols)
    for character in lower_text:
        if character in char_counts:
            char_counts[character] += 1
    
    # Filter the dictionary to include only letters with counts greater than one
    repeated_letters = {char: count for char, count in char_counts.items() if count > 1}

    return repeated_letters

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string. The letter 'a' appears often."
    
    result_dict = find_repeated_letters(sample_string)
    
    print(result_dict)