import re

def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a list of unique letters that appear at least twice in the input string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    The function converts the text to lowercase for uniform processing, filters out 
    non-alphabetic characters (optional based on strict interpretation), but since the task 
    specifies "letters", we consider only alphabets. Duplicate letters are identified regardless of case.

    Args:
        text (str): Input string containing any mixture of characters.

    Returns:
        list[str]: Sorted list of unique lower-case letters that appear at least twice in `text`.
    
    Example:
        >>> find_duplicate_letters("Hello, World!")
        ['e', 'h', 'l', 'o'] (Note: 'd' and 'w' are not repeated)

        Actually for "Hello, World!": 
        H/h -> 2, e -> 1, l/l/l -> 3, o/o -> 2, W/w -> 1
        So duplicates: h, l, o
    
    >>> find_duplicate_letters("Aa bb CC dd")
        ['a', 'b', 'c']

    Note: Non-alphabetic characters are ignored as per the definition of "letters".
    """
    
    # Convert string to lowercase and extract only alphabetic characters
    cleaned_text = ''.join(ch.lower() for ch in text if ch.isalpha())
    
    letter_counts = {}
    
    # Count frequency of each letter
    for char in cleaned_text:
        if char not in letter_counts:
            letter_counts[char] = 0
        letter_counts[char] += 1
    
    # Collect letters with count >= 2 and sort them alphabetically
    duplicates = [letter for letter, count in letter_counts.items() if count >= 2]
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_inputs = [
        "Hello, World!",
        "Aa bb CC dd",
        "Python Programming is Fun!!",
        "The quick brown fox jumps over the lazy dog.",
        "aaaaabbbbcccc"
    ]

    print("Testing find_duplicate_letters function:")
    
    for sample in sample_inputs:
        result = find_duplicate_letters(sample)
        # Format output nicely, e.g., as a string representation or just list items separated by comma and space
        formatted_result = ', '.join(result) if isinstance(result, list) else str(result)
        print(f"Input: '{sample}'")
        print("Duplicates:", result)
        
        # Verify against expected logic manually to avoid markdown prose outside code block