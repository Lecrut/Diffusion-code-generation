def find_duplicate_letters(s: str) -> list[str]:
    """
    Returns a sorted list of unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        List[str]: A sorted list of uppercase unique letters found more than once.
    """
    # Convert string to lowercase for case-insensitive comparison
    lower_s = s.lower()
    
    letter_counts = {}
    
    # Count occurrences of each character (ignoring non-alphabetic characters)
    for char in lower_s:
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    # Collect letters that appear at least twice and sort them alphabetically
    duplicate_letters = sorted([letter for letter, count in letter_counts.items() if count >= 2])
    
    return duplicate_letters

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "A man a plan a canal Panama",
        "Python Programming",
        "123 !@# abcABC"
    ]
    
    for test_str in sample_strings:
        result = find_duplicate_letters(test_str)
        print(f"'{test_str}' -> {result}")