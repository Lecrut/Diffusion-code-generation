def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a list of all unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of uppercase letters found more than once.
    """
    # Convert the string to lowercase for case-insensitive comparison
    lower_text = text.lower()
    
    # Dictionary to count occurrences of each letter (ignoring non-alphabetic characters)
    char_count = {}
    
    for char in lower_text:
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are counted
            char_count[char] = char_count.get(char, 0) + 1
            
    # Filter letters that appear more than once and convert to uppercase
    duplicate_letters = [char.upper() for char in char_count if char_count[char] > 1]
    
    return sorted(duplicate_letters)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "A man a plan a canal Panama",
        "Python Programming Language",
        "The quick brown fox jumps over the lazy dog"
    ]

    for test_string in sample_strings:
        result = find_duplicate_letters(test_string)
        print(f"Input: '{test_string}'")
        print(f"Duplicate letters: {result}")
        print("-" * 30)