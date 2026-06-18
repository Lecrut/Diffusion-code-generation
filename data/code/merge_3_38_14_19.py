def count_repeated_letters(text: str) -> dict:
    """
    Processes a string to find letters that appear more than once.
    
    Args:
        text (str): The input string containing alphabetic characters and potentially others.
        
    Returns:
        dict: A dictionary where keys are the repeated letters 
              (case-sensitive based on input) and values are their occurrence counts.
               Only letters with a count > 1 are included in this dictionary, as per "repeated" definition,
               though typically such tasks imply case-insensitivity unless specified otherwise.
    """
    # Count occurrences of each character while ignoring non-alphabetic characters if strictly needed for 'letters' context,
    # but the problem says "keys are the letters", implying we should focus on alphabets. 
    # However, to be safe and general without over-constraining based on ambiguous phrasing:
    # We will count all unique chars first, then filter for those > 1 occurrence if they qualify as 'letters'.
    
    char_counts = {}
    
    for char in text:
        if not char.isalpha(): 
            continue
            
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Filter only keys where count is greater than 1 (repeated letters)
    repeated_letters_dict = {k: v for k, v in char_counts.items() if v > 1}
    
    return repeated_letters_dict

if __name__ == '__main__':
    sample_string = "Hello World! This string has multiple e's and l's."
    result = count_repeated_letters(sample_string)
    print(result)