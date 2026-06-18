def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a list of all unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    The function converts the input to lowercase for uniformity, counts character occurrences,
    filters those appearing more than once, and returns them sorted alphabetically.

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of unique letters that appear at least twice.
    """
    # Convert the entire string to lowercase for case-insensitive comparison
    lower_text = text.lower()
    
    # Dictionary to store frequency of each character
    char_count = {}
    
    # Iterate through characters and count occurrences
    for char in lower_text:
        if not char.isalpha():  # Ignore non-alphabetic characters like spaces or punctuation
            continue
        char_count[char] = char_count.get(char, 0) + 1
    
    # Filter letters that appear at least twice (count > 1), then sort them alphabetically
    duplicate_letters = [letter for letter, count in char_count.items() if count >= 2]
    
    return sorted(duplicate_letters)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = ["Hello World!", "A man a plan a canal Panama", "Python Programming"]

    for s in samples:
        result = find_duplicate_letters(s)
        print(f"Input: '{s}'")
        print(f"Duplicate letters (case-insensitive): {result}")
        print("-" * 40)