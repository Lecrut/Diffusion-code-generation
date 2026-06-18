import string

def find_repeated_letters(text):
    """
    Identifies all letters that appear more than once in the input text, 
    regardless of their case (e.g., 'A' and 'a' are treated as the same).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found.
    """
    # Dictionary to track letter counts, case-insensitive
    char_count = {}
    
    for ch in text.lower():
        if ch.isalpha() and len(ch) == 1:
            count = char_count.get(ch, 0) + 1
            char_count[ch] = count
            
    # Extract letters with a count greater than 1
    repeated_letters = [letter for letter, count in char_count.items() if count > 1]
    
    return sorted(repeated_letters)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string where the letters 'a', 'e' and 'l' are repeated multiple times."
    
    result = find_repeated_letters(sample_text)
    
    print(f"Input text: '{sample_text}'")
    if not result:
        print("No repeated letters found.")
    else:
        print(f"Repeated letters found in the string: {', '.join(result)}")