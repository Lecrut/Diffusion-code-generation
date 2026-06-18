def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    It uses a dictionary to count occurrences for O(n) time complexity.

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set of unique letters found more than once in the string.
    """
    letter_counts = {}
    
    # Iterate over each character, converting to lowercase for case-insensitivity
    for char in text.lower():
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are counted
            count = letter_counts.get(char, 0) + 1
            letter_counts[char] = count
            
    # Collect letters with a count greater than 1 into the result set
    repeated_letters = {char for char, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_input = "Hello World! This is an example of finding repeated letters."
    result = find_repeated_letters(sample_input)
    print(f"Repeated letters: {sorted(result)}")