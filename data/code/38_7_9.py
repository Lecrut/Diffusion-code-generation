def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a sorted list of unique lowercase letters that appear at least twice in the input string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        List[str]: A sorted list of unique lowercase letters found more than once.
    """
    letter_count = {}
    
    # Iterate over each character, converting uppercase to lowercase for case-insensitivity
    for char in text.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            letter_count[char] = letter_count.get(char, 0) + 1
            
    # Filter letters that appear at least twice and return them sorted
    duplicates = [letter for letter, count in letter_count.items() if count >= 2]
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "Hello World! This is a test. Aa bb CC."
    result = find_duplicate_letters(sample_string)
    print(result)