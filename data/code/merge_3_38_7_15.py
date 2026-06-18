def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a list of unique letters that appear at least twice in the input string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    The returned list will contain lowercase versions of these letters only once per unique character.

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of unique lower-case letters appearing at least twice.
    """
    if not text:
        return []
    
    # Normalize the text to lowercase and count frequencies
    normalized_text = "".join(char.lower() for char in text)
    letter_counts = {}
    
    for char in normalized_text:
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    # Filter letters that appear at least twice and return them sorted
    duplicates = [letter for letter, count in letter_counts.items() if count >= 2]
    
    # Since dictionaries maintain insertion order from Python 3.7+, 
    # we can sort the result explicitly to ensure consistent output regardless of input order
    duplicates.sort(key=lambda x: ord(x))
    
    return duplicates

if __name__ == '__main__':
    sample_string = "Hello, World! Hello Again."
    unique_duplicates = find_duplicate_letters(sample_string)
    
    # Output the result directly without user prompts or file I/O
    print(f"Input string: {sample_string}")
    print("Unique letters appearing at least twice (case-insensitive):")
    for letter in unique_duplicates:
        print(letter, end=" ")