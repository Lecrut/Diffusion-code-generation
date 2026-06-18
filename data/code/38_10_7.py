def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input string.
    
    The function is case-insensitive, meaning 'A' and 'a' are treated as 
    the same letter. Non-alphabetic characters (digits, punctuation, spaces) 
    are ignored during counting but do not affect the output unless they 
    were part of a repeated sequence involving letters (which this logic does 
    not support; it strictly checks for repeated alphabetic characters).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique lowercase letters that are repeated.
                   If no letters are repeated, returns an empty list.
    """
    letter_counts = {}

    # Iterate over each character in the string
    for char in text:
        if 'a' <= char.lower() <= 'z':  # Check if it's a lowercase alphabetic character
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1

    repeated_letters = []
    
    # Collect letters that have been counted more than once
    for letter in letter_counts:
        if letter_counts[letter] > 1:
            repeated_letters.append(letter)

    return sorted(repeated_letters)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Python Programming",
        "A man a plan a canal Panama",
        "The quick brown fox jumps over the lazy dog"
    ]

    for test_input in sample_strings:
        result = find_repeated_letters(test_input)
        if not result:
            print(f"No repeated letters found in '{test_input}'")
        else:
            # Convert to uppercase for display as per common convention, 
            # though the internal logic is case-insensitive.
            formatted_result = [letter.upper() for letter in result]
            print(f"Repeated letters in '{test_input}': {', '.join(formatted_result)}")